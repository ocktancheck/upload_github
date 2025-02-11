# Telegram Saver: Ваш Личный Архивировщик

Этот мощный скрипт на Python, использующий библиотеку Telethon, позволяет вам легко сохранять все файлы и сообщения из вашего Telegram-аккаунта (Избранное) или любого чата/канала, к которому у вас есть доступ!

Для чего это нужно?

* Создание резервных копий:  Надежно сохраняйте важные переписки, файлы, фотографии, видео и другие данные из Telegram.
* Освобождение места:  Очистите "Избранное" или другие чаты.
* Офлайн-доступ:  Доступ к данным без интернета.
* Архивирование проектов:  Сохраняйте рабочие переписки.
* Личный архив: Создайте свою библиотеку.

Особенности

* Сохранение ВСЕГО:  Все типы файлов и текстовые сообщения.
* Уникальные имена файлов:  Предотвращение конфликтов.
* Работа с "Избранным" и любыми чатами:  По ID чата.
* Автоматическая отправка архива:  В "Избранное".
* Удаление временных файлов:  После отправки.
* Красивый прогресс-бар:  В консоли.
* Обработка ошибок:  Информативные сообщения.
* Кроссплатформенность: Windows, macOS, Linux, Android (Termux и Pydroid 3).
* Простота использования:  Команда .save.

Установка и Настройка

0. Требования

* Python 3.7 или новее (с добавлением в PATH).
* Установщик пакетов pip.

1. Установка Telethon и зависимостей:

pip install telethon tqdm colorama

* telethon:  Взаимодействие с Telegram API.
* tqdm:  Прогресс-бар.
* colorama:  Цветной вывод.

2. Получение API ID и API Hash:

1. my.telegram.org -> Вход.
2. "API development tools".
3. Создайте приложение (любые данные).
4. Получите api_id (число) и api_hash (строка). Сохраните!

3. Загрузка и настройка скрипта:

1. Скачайте скрипт:  Скопируйте код в файл telegram_saver.py.
2. Отредактируйте:

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
session_name = 'my_telegram_session'

    * Замените YOUR_API_ID на ваш api_id.
    * Замените 'YOUR_API_HASH' на ваш api_hash.
    * session_name оставьте или измените.

4. Запуск скрипта:

Windows:

1. Командная строка (cmd).
2. cd в папку со скриптом:

cd C:\Users\YourName\Documents\TelegramSaver

3. Запуск:

python telegram_saver.py

macOS / Linux:

1. Терминал.
2. cd:

cd /Users/YourName/Documents/TelegramSaver  # macOS
cd /home/YourName/Documents/TelegramSaver  # Linux

3. Запуск:

python3 telegram_saver.py

Android (Termux):

1. Установите Termux.
2. Python:

pkg install python

3. Пакеты:

pip install telethon tqdm colorama

4. Загрузите скрипт.
5. cd:

cd /sdcard/Download

6. Запуск:

python telegram_saver.py

Android (Pydroid 3):

1. Установите Pydroid 3.
2. Установите Repository Plugin.
3. Pip -> Установите telethon, tqdm, colorama.
4. Загрузите скрипт.
5. Запустите.

5. Первый запуск:

* Введите номер телефона и код подтверждения.
* Создастся файл сессии.

Использование

1. Запустите скрипт.
2. Отправьте .save в Telegram (для "Избранного").
3. Для других чатов: .save -1001234567890 (с ID чата).

Документация

* api_id: Ваш API ID.
* api_hash: Ваш API hash.
* session_name: Имя файла сессии.
* save_messages_to_txt(...): Сохраняет текст.
* generate_unique_filename(...): Уникальные имена.
* download_and_zip(...): Скачивает и архивирует.
* @client.on(...): Обрабатывает .save.
    * pattern=r'^\.save ?(-?\d*)'`: Регулярное выражение.
* async def save_handler(...): Обработчик команды.
* async def main():`: Запуск клиента.
* if __name__ == "__main__":`: Запуск скрипта.

Вклад

Fork, изменения, pull request.

Предупреждение

* На свой страх и риск.
* Соблюдайте правила Telegram.
* Не передавайте api_id, api_hash, файл сессии.

Лицензия

MIT.  LICENSE (файл).