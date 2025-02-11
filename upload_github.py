import os
import requests
import json
import base64
import getpass

# --- Глобальные переменные и константы ---
CONFIG_FILE = "info.txt"
DEFAULT_LANGUAGE = "en"
IGNORED_DIRS = [".git", ".idea", "__pycache__", ".vscode", "node_modules", ".svn"]  # Папки для игнорирования
IGNORED_FILES = [] # Можете добавить и файлы


# --- Классы для текстов на разных языках ---

class Texts:
    def __init__(self):
        self.texts = {
            "en": {
                "enter_token": "Please enter your GitHub Personal Access Token (with 'repo' scope): ",
                "token_link": "You can create one here: https://github.com/settings/tokens/new (select 'repo' scope)",
                "token_saved": "Token saved for future use.",
                "use_saved_token": "Use saved token (y/n)? ",
                "enter_new_token": "Enter new token: ",
                "invalid_token": "Invalid token. Please try again.",
                "your_repos": "\nYour repositories:",
                "choose_repo": "\nChoose a repository (enter number) or enter 'new' to create a new one:",
                "invalid_choice": "Invalid choice.",
                "new_repo_name": "Enter the name of the new repository: ",
                "private_repo": "Make the repository private? (y/n): ",
                "create_readme": "Create an empty README.md file? (y/n): ",  # Добавлено
                "repo_created": "Repository created successfully.",
                "file_uploaded": "File {} successfully uploaded/updated.",
                "file_error": "Error uploading file {}: {} - {}",
                "upload_complete": "\nUpload complete.",
                "choose_language": "Choose language / Выберите язык:\n1. English (en)\n2. Русский (ru)\n> ",
                "invalid_language": "Invalid language choice.  Using English.",
                "language_saved": "Language saved.",
                "file_exists": "File {} already exists in the repository. Overwrite? (y/n/a): ",
                "overwrite": "Overwrite",
                "skip": "Skip",
                "apply_to_all": "Apply to all",
                "yes": "y",
                "no": "n",
                "all": "a",
            },
            "ru": {
                "enter_token": "Пожалуйста, введите ваш персональный токен доступа GitHub (с правами 'repo'): ",
                "token_link": "Вы можете создать его здесь: https://github.com/settings/tokens/new (выберите 'repo')",
                "token_saved": "Токен сохранен для будущего использования.",
                "use_saved_token": "Использовать сохраненный токен (y/n)? ",
                "enter_new_token": "Введите новый токен: ",
                "invalid_token": "Неверный токен. Пожалуйста, попробуйте снова.",
                "your_repos": "\nВаши репозитории:",
                "choose_repo": "\nВыберите репозиторий (введите номер) или введите 'new' для создания нового:",
                "invalid_choice": "Неверный выбор.",
                "new_repo_name": "Введите имя нового репозитория: ",
                "private_repo": "Сделать репозиторий приватным? (y/n): ",
                "create_readme": "Создать пустой файл README.md? (y/n): ",  # Добавлено
                "repo_created": "Репозиторий успешно создан.",
                "file_uploaded": "Файл {} успешно загружен/обновлен.",
                "file_error": "Ошибка при загрузке файла {}: {} - {}",
                "upload_complete": "\nЗагрузка завершена.",
                "choose_language": "Choose language / Выберите язык:\n1. English (en)\n2. Русский (ru)\n> ",
                "invalid_language": "Неверный выбор языка.  Используется английский.",
                "language_saved": "Язык сохранен.",
                "file_exists": "Файл {} уже существует в репозитории.  Перезаписать? (y/n/a): ",
                "overwrite": "Перезаписать",
                "skip": "Пропустить",
                "apply_to_all": "Применить ко всем",
                "yes": "y", #английская
                "no": "n", #английская
                "all": "a", #английская
            }
        }

    def get(self, key, lang="en"):
        """Получает текст по ключу и языку."""
        return self.texts.get(lang, self.texts["en"]).get(key, key)  # Возвращает ключ, если текст не найден

# --- Функции для работы с конфигурацией ---

def load_config():
    """Загружает конфигурацию из файла."""
    config = {"language": DEFAULT_LANGUAGE, "token": ""}
    try:
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                key, value = line.strip().split(":", 1)  # Разделяем только по первому ":"
                config[key] = value
    except FileNotFoundError:
        pass  # Файла конфигурации еще нет
    return config

def save_config(config):
    """Сохраняет конфигурацию в файл."""
    with open(CONFIG_FILE, "w") as f:
        for key, value in config.items():
            f.write(f"{key}:{value}\n")

# --- Функции для работы с GitHub API ---

def get_github_token(texts, current_lang):
    """Запрашивает токен GitHub у пользователя."""
    config = load_config()
    if config["token"]:
        use_saved = input(texts.get("use_saved_token", current_lang)).strip().lower()
        if use_saved == texts.get("yes",current_lang):
            return config["token"]
    print(texts.get("enter_token", current_lang))
    print(texts.get("token_link", current_lang))
    while True:
        token = getpass.getpass(texts.get("enter_new_token", current_lang))
        if token:
             # Валидация токена (простейшая)
            headers = {"Authorization": f"token {token}"}
            response = requests.get("https://api.github.com/user", headers=headers)
            if response.status_code == 200:
                config["token"] = token
                save_config(config)
                print(texts.get("token_saved", current_lang))
                return token
            else:
                print(texts.get("invalid_token", current_lang))
        else:
           print(texts.get("invalid_token", current_lang))

def get_user_repositories(token, texts, current_lang):
    """Получает список репозиториев пользователя."""
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.get("https://api.github.com/user/repos", headers=headers)
    response.raise_for_status()
    return response.json()

def choose_repository(token, texts, current_lang):
    """Позволяет пользователю выбрать репозиторий или создать новый."""
    repos = get_user_repositories(token, texts, current_lang)
    print(texts.get("your_repos", current_lang))
    for i, repo in enumerate(repos):
        print(f"{i + 1}. {repo['name']} ({repo['full_name']})")

    print(texts.get("choose_repo", current_lang))
    choice = input("> ").strip()

    if choice.lower() == 'new':
        repo_name = input(texts.get("new_repo_name", current_lang))
        private = input(texts.get("private_repo", current_lang)).strip().lower() == texts.get("yes",current_lang)
        create_readme_choice = input(texts.get("create_readme", current_lang)).strip().lower() == texts.get("yes",current_lang) #Добавили выбор
        return create_repository(token, repo_name, private, create_readme_choice, texts, current_lang)  # Передаем create_readme_choice
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(repos):
                return repos[index]
            else:
                print(texts.get("invalid_choice", current_lang))
                return None
        except ValueError:
            print(texts.get("invalid_choice", current_lang))
            return None

def create_repository(token, repo_name, private=False, create_readme=True, texts=None, current_lang="en"):
    """Создает новый репозиторий.  Добавлен параметр create_readme."""
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {
        "name": repo_name,
        "private": private,
        "auto_init": create_readme,  # Используем параметр create_readme
    }
    response = requests.post("https://api.github.com/user/repos", headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(texts.get("repo_created", current_lang)) #Выводим сообщение
    return response.json()

def upload_file_to_github(token, repo_full_name, file_path, branch="main", texts=None, current_lang="en"):
    """Загружает один файл в репозиторий GitHub."""
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

    # 1. Получаем SHA файла, если он существует
    get_content_url = f"https://api.github.com/repos/{repo_full_name}/contents/{file_path}"
    response = requests.get(get_content_url, headers=headers)

    sha = None
    if response.status_code == 200:
        sha = response.json()['sha']
    elif response.status_code != 404:
        print(texts.get("file_error", current_lang).format(file_path, response.status_code, response.text))
        return False

    # 2. Подготовка данных
    with open(file_path, "rb") as f:
        content = f.read()
    encoded_content = base64.b64encode(content).decode("utf-8")

    data = {"message": f"Add/Update {file_path}", "content": encoded_content, "branch": branch}
    if sha:
        data["sha"] = sha

    # 3. Загрузка файла
    put_url = f"https://api.github.com/repos/{repo_full_name}/contents/{file_path}"
    response = requests.put(put_url, headers=headers, data=json.dumps(data))
    if response.status_code in (200, 201):
        print(texts.get("file_uploaded", current_lang).format(file_path))
        return True
    else:
        print(texts.get("file_error", current_lang).format(file_path, response.status_code, response.text))
        return False


def upload_directory_to_github(token, repo_full_name, local_dir, branch="main", texts=None, current_lang="en", apply_all_choice=None):
    """Рекурсивно загружает файлы и папки, обрабатывая конфликты."""
    for item in os.listdir(local_dir):
        item_path = os.path.join(local_dir, item)
        relative_path = os.path.relpath(item_path, start=os.path.dirname(__file__)).replace("\\", "/")

        if item_path == __file__ or item in IGNORED_FILES:  # Исключаем сам скрипт
            continue
        if os.path.isdir(item_path):
            if item in IGNORED_DIRS: #Добавили игнорирование папок
                continue
            upload_directory_to_github(token, repo_full_name, item_path, branch, texts, current_lang, apply_all_choice) #Передаем apply_all_choice

        elif os.path.isfile(item_path):
            # Проверка на конфликт и запрос действия
            file_exists_url = f"https://api.github.com/repos/{repo_full_name}/contents/{relative_path}"
            headers = {"Authorization": f"token {token}"}
            response = requests.get(file_exists_url, headers=headers)

            if response.status_code == 200:  # Файл существует
                if apply_all_choice == "overwrite":
                     upload_file_to_github(token, repo_full_name, relative_path, branch, texts, current_lang)
                elif apply_all_choice == "skip":
                    continue
                else:

                    choice = input(texts.get("file_exists", current_lang).format(relative_path)).strip().lower()
                    if choice == texts.get("yes",current_lang) or choice == texts.get("overwrite",current_lang):
                        upload_file_to_github(token, repo_full_name, relative_path, branch, texts, current_lang)
                    elif choice == texts.get("all",current_lang) or choice == texts.get("apply_to_all",current_lang):
                        apply_all_choice = "overwrite"
                        upload_file_to_github(token, repo_full_name, relative_path, branch, texts, current_lang)
                    elif choice == texts.get("no",current_lang) or choice == texts.get("skip",current_lang):
                        continue #Пропускаем
                    else:
                        print(texts.get("invalid_choice", current_lang)) #Если неверный ввод, то пропускаем
                        continue

            elif response.status_code == 404:
                # Файла нет, загружаем
                upload_file_to_github(token, repo_full_name, relative_path, branch, texts, current_lang)
            else:
                # Другая ошибка
                 print(texts.get("file_error", current_lang).format(relative_path, response.status_code, response.text))
                 return False


# --- Основная функция ---

def main():
    """Основная функция скрипта."""
    texts = Texts()
    config = load_config()
    current_lang = config["language"]

    # Выбор языка (только если язык не был сохранен)
    if current_lang == DEFAULT_LANGUAGE:  # Проверяем, что язык по умолчанию
        while True:
            lang_choice = input(texts.get("choose_language")).strip().lower()
            if lang_choice in ("1", "en"):
                current_lang = "en"
                break
            elif lang_choice in ("2", "ru"):
                current_lang = "ru"
                break
            else:
                print(texts.get("invalid_language", "en")) #Если язык неверный то ставим английский
        config["language"] = current_lang
        save_config(config)
        print(texts.get("language_saved", current_lang))

    token = get_github_token(texts, current_lang)
    if not token:
        return

    repo_info = choose_repository(token, texts, current_lang)
    if not repo_info:
        return

    repo_full_name = repo_info['full_name']
    local_directory = os.path.dirname(__file__)
    upload_directory_to_github(token, repo_full_name, local_directory, texts=texts, current_lang=current_lang)

    print(texts.get("upload_complete", current_lang))

if __name__ == "__main__":
    main()