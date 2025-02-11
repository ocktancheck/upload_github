import asyncio
import zipfile
import time
from datetime import datetime
from telethon import TelegramClient, events, types
import os
import glob
from tqdm import tqdm
from colorama import Fore, Style, init

# Инициализируем colorama
init(autoreset=True)

# Замените на свои API ID и API hash
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# Имя файла сессии
session_name = 'my_telegram_session'

client = TelegramClient(session_name, api_id, api_hash)

async def save_messages_to_txt(messages, filename):
    """Сохраняет сообщения в текстовый файл."""
    with open(filename, "w", encoding="utf-8") as f:
        for message in messages:
            if message.text:
                date_time_str = message.date.strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{date_time_str}\n")
                f.write(f"{message.text}\n")
                f.write("_________________________\n")

def generate_unique_filename(filename):
    """Генерирует уникальное имя файла."""
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filename):
        filename = f"{base}_{counter}{ext}"
        counter += 1
        if counter > 10:
            return None
    return filename

async def download_and_zip(entity, zip_filename):
    """Скачивает файлы, сохраняет в ZIP."""
    downloaded_filenames = []

    try:
        messages = await client.get_messages(entity, limit=None)
    except (ValueError, Exception) as e:
        print(f"{Fore.RED}Ошибка: {e}{Style.RESET_ALL}")
        return False, []

    if not messages:
        print(f"{Fore.YELLOW}Нет сообщений.{Style.RESET_ALL}")
        return False, []

    unique_zip_filename = generate_unique_filename(zip_filename)
    if not unique_zip_filename:
        print(f"{Fore.RED}Не удалось сгенерировать имя ZIP.{Style.RESET_ALL}")
        return False, []

    with zipfile.ZipFile(unique_zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        await save_messages_to_txt(messages, "messages.txt")
        zipf.write("messages.txt")
        downloaded_filenames.append("messages.txt")

        with tqdm(total=len(messages), desc=f"{Fore.CYAN}Обработка{Style.RESET_ALL}", unit="msg",
                  bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]",
                  colour="green") as pbar:
            for message in reversed(messages):
                # Проверяем, является ли сообщение системным
                if isinstance(message, types.MessageService):
                    pbar.update(1)  # Обновляем прогресс-бар, но не обрабатываем
                    continue  # Пропускаем системные сообщения

                if message.media:
                    try:
                        file_path = None
                        original_filename = "unknown"

                        if isinstance(message.media, types.MessageMediaDocument):
                            if message.media.document:
                                for attr in message.media.document.attributes:
                                    if isinstance(attr, types.DocumentAttributeFilename):
                                        original_filename = attr.file_name
                                        break
                                if original_filename == "unknown":
                                    ext = ""
                                    if message.media.document.mime_type:
                                        ext = "." + message.media.document.mime_type.split('/')[-1]
                                        if ext == ".ogg": ext = ".oga"
                                        if ext == ".plain": ext = ".txt"
                                        if ext == ".javascript": ext = ".js"
                                    original_filename = message.date.strftime("%Y-%m-%d_%H-%M-%S") + ext
                            original_filename = generate_unique_filename(original_filename)
                            if not original_filename:
                                continue

                            file_path = await message.download_media(file=original_filename)

                        elif hasattr(message.media, 'photo') and message.media.photo:
                            original_filename = message.date.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
                            original_filename = generate_unique_filename(original_filename)
                            if not original_filename:
                                continue
                            file_path = await message.download_media(file=original_filename)

                        elif isinstance(message.media, types.MessageMediaWebPage):
                            pass
                        else:
                            pass

                        if file_path:
                            zipf.write(file_path)
                            downloaded_filenames.append(original_filename)

                    except Exception as e:
                        pass

                pbar.update(1)

    return True, downloaded_filenames, unique_zip_filename


@client.on(events.NewMessage(pattern=r'^\.save ?(-?\d*)'))
async def save_handler(event):
    """Обрабатывает .save, отправляет архив, удаляет."""
    chat_id = event.pattern_match.group(1)

    if not chat_id:
        entity = "me"
        zip_filename = "saved.zip"
        print(f"{Fore.GREEN}Сохранение из Избранного...{Style.RESET_ALL}")
    else:
        try:
            chat_id = int(chat_id)
            entity = await client.get_entity(chat_id)
            zip_filename = f"{chat_id}.zip"
            print(f"{Fore.GREEN}Сохранение из чата ID: {chat_id}...{Style.RESET_ALL}")
        except (ValueError, Exception) as e:
            await event.reply(f"Ошибка: {e}")
            print(f"{Fore.RED}Ошибка: {e}{Style.RESET_ALL}")
            return

    success, downloaded_filenames, unique_zip_filename = await download_and_zip(entity, zip_filename)

    if success:
        try:
            await asyncio.sleep(2)
            await client.send_file("me", unique_zip_filename)
            await event.reply(f"Архив {unique_zip_filename} отправлен.")

            try:
                if os.path.exists(unique_zip_filename):
                    os.remove(unique_zip_filename)
                for filename in downloaded_filenames:
                    for file_path in glob.glob(filename.split('.')[0] + '*'):
                        if os.path.exists(file_path):
                            os.remove(file_path)

            except Exception as e:
                print(f"{Fore.RED}Ошибка удаления: {e}{Style.RESET_ALL}")
                await event.reply(f"Ошибка удаления: {e}")

        except Exception as e:
            await event.reply(f"Ошибка отправки: {e}")
            print(f"{Fore.RED}Ошибка: {e}{Style.RESET_ALL}")
            try:
                if os.path.exists(unique_zip_filename):
                    os.remove(unique_zip_filename)
                for filename in downloaded_filenames:
                    for file_path in glob.glob(filename.split('.')[0] + '*'):
                        if os.path.exists(file_path):
                            os.remove(file_path)
            except Exception as e:
                print(f"{Fore.RED}Ошибка удаления: {e}{Style.RESET_ALL}")
    else:
        await event.reply("Не удалось создать.")
        return

    print(f"{Fore.GREEN}Готово.{Style.RESET_ALL}")

async def main():
    await client.start()
    print(f"{Fore.GREEN}Клиент запущен. Ожидание .save...{Style.RESET_ALL}")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())