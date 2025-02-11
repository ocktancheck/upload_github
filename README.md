# 🚀 Загрузчик файлов на GitHub: Ваш мультиязычный помощник! 🚀

Этот скрипт на Python – ваш незаменимый инструмент для легкой и быстрой загрузки файлов и папок (включая все вложенные подпапки!) прямо в репозиторий GitHub. ✨ Благодаря использованию GitHub API, скрипт обеспечивает максимальную надежность и безопасность. Скрипт поддерживает **русский** и **английский** языки!

**Скрипт 100% находится в этом репозитории: [https://github.com/ocktancheck/upload_github.git](https://github.com/ocktancheck/upload_github.git)**. Вам не нужно ничего менять в ссылках!

## 📖 Подробный туториал по использованию

### 🛠️ Подготовка и установка: Шаг за шагом

#### Для всех операционных систем (общие шаги):

1.  **📥 Скачивание скрипта:**

    Есть два основных способа (выберите один):

    **Способ 1: С помощью Git (рекомендуется):**

    *   **Что такое Git?** Git – это система контроля версий (как Time Machine, но для кода). GitHub построен на основе Git.
    *   **Зачем использовать Git?** Легко обновлять скрипт; надежно.
    *   **Установка Git:**
        *   **Windows:** Скачайте и установите Git с сайта: [https://git-scm.com/download/win](https://git-scm.com/download/win).
        *   **macOS:**
            ```bash
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  # Установите Homebrew
            brew install git # Установите Git
            ```
        *   **Linux:** Используйте менеджер пакетов (например, `sudo apt install git` для Ubuntu/Debian).
        *   **Android (Termux):** `pkg install git`
    *   **Как скачать (если Git установлен):**
        1.  Откройте командную строку/терминал.
        2.  Перейдите в папку, куда хотите скачать: `cd /path/to/your/folder`.
        3.  Склонируйте репозиторий:
            ```bash
            git clone https://github.com/ocktancheck/upload_github.git
            ```
        4.  Перейдите в папку: `cd upload_github`

    **Способ 2: С сайта GitHub (вручную):**

    1.  Откройте репозиторий: [https://github.com/ocktancheck/upload_github.git](https://github.com/ocktancheck/upload_github.git).
    2.  Нажмите зеленую кнопку "Code".
    3.  Выберите "Download ZIP".
    4.  Распакуйте архив.

2.  **🔑 Создание персонального токена GitHub (Personal Access Token/PAT):**

    *   **Зачем?** Токен – это безопасный ключ к вашему аккаунту.
    *   **Как создать (подробно):**
        1.  **Войдите в GitHub:** [https://github.com/](https://github.com/).
        2.  **Настройки:** Аватар (справа вверху) -> "Settings".
        3.  **Developer settings:** Внизу слева.
        4.  **Personal access tokens** -> "Tokens (classic)".
        5.  **Generate new token** -> "Generate new token (classic)".
        6.  **Заполните:**
            *   **Note:** Имя (например, "GitHub Uploader").
            *   **Expiration:** *Рекомендуется* срок действия (например, 30 дней).
            *   **Select scopes:** **ВАЖНО!** *Только* `repo`. *Не давайте лишних прав!*
        7.  **Generate token**.
        8.  **Сразу же скопируйте и сохраните токен!** GitHub покажет его *только один раз*.

#### Установка и запуск (по платформам):

##### Windows:

1.  **🐍 Python:**
    *   Скачайте с [https://www.python.org/downloads/](https://www.python.org/downloads/) (3.6+).
    *   Запустите установщик. **ВАЖНО!** Отметьте **"Add Python 3.x to PATH"**.
    *   Проверка: Командная строка (Win + R, `cmd`, Enter) -> `python --version` (или `py --version`).

2.  **📦 requests:**
    *   Командная строка: `pip install requests` (или `python -m pip install requests`, `py -m pip install requests`).

3.  **🚀 Запуск:**
    1.  Командная строка.
    2.  `cd` в папку со скриптом (например, `cd upload_github`).
    3.  `python upload_github.py` (или `py upload_github.py`).
    4.  Введите токен.
    5.  Выберите/создайте репозиторий.

##### Linux/macOS:

1.  **🐍 Python:**
    *   **Linux:**  `python3 --version`. Если нет:
        *   Ubuntu/Debian: `sudo apt update && sudo apt install python3`
        *   Fedora/CentOS/RHEL: `sudo dnf install python3`
        *   Arch: `sudo pacman -S python`
    *   **macOS:**
        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # Homebrew
        brew install python # Python
        ```

2.  **📦 requests:**
    *   Терминал: `pip3 install requests`

3.  **🚀 Запуск:**
    1.  Терминал.
    2.  `cd` в папку: `cd upload_github`
    3.  `python3 upload_github.py`
    4.  Токен -> репозиторий.

##### Android (Termux):

1.  **🐍 Python:**
    *   Установите Termux (Google Play/F-Droid).
    *   Termux: `pkg update && pkg install python`
    *   `python --version`

2.  **📦 requests:**
    *   `pip install requests`

3.  **📥 Скачивание (в Termux):**
     *   **Git (рекомендуется):**
        ```bash
        pkg install git
        git clone https://github.com/ocktancheck/upload_github.git
        cd upload_github
        ```

4.  **🚀 Запуск:**
    1.  `cd upload_github`
    2.  `python upload_github.py`

##### Android (Pydroid 3):

1.  **🐍 Python:** Уже встроен в Pydroid 3.

2.  **📦 requests:** Pydroid 3 -> Меню -> "Pip" -> `requests`.

3.  **📥 Скачивание:**
    *   **Простой способ:** Скачайте ZIP (браузер) -> откройте `.py` в Pydroid 3.
    *   **Git (сложнее):** Pydroid 3 -> Терминал -> `pip install gitpython` -> `git clone ...`

4.  **🚀 Запуск:** Откройте `.py` -> желтая кнопка запуска.

### ⚙️ Использование скрипта:

1.  **Выбор языка:** При первом запуске скрипт предложит выбрать язык (русский/английский). Выбранный язык сохранится.
2.  **Токен:**
    *   Скрипт спросит, использовать ли сохраненный токен.
    *   Если нет/токена нет, введите новый. Токен сохранится.
3.  **Репозиторий:**
    *   Выберите из списка (введите номер) или создайте новый (`new`).
    *   При создании:
        *   Имя репозитория.
        *   Приватный? (y/n).
        *   Создать пустой README.md? (y/n).
4.  **Загрузка:** Скрипт загрузит файлы/папки.
5.  **Конфликты:** Если файл уже существует, скрипт спросит:
    *   Перезаписать (y/overwrite).
    *   Пропустить (n/skip).
    *   Применить ко всем (a/apply to all).

### 💻 Платформо-зависимые особенности

*   **Windows:** PATH, кодировка (`chcp 65001`).
*   **Linux/macOS:** Права (`chmod +x`).
*   **Termux:** `termux-setup-storage`, SD-карта (root?).
*   **Pydroid 3:** Ограниченный доступ к файловой системе.

## 📜 Документация

*   `get_github_token()`: Запрос токена.
*   `get_user_repositories(token)`: Список репозиториев.
*   `choose_repository(token)`: Выбор/создание репозитория.
*   `create_repository(token, repo_name, private, create_readme)`: Создание.
*   `upload_file_to_github(token, repo_full_name, file_path, branch, texts, current_lang)`: Загрузка файла.
*   `upload_directory_to_github(...)`: Рекурсивная загрузка.
*   `main()`: Запуск.

## ❓ FAQ

*   **"ModuleNotFoundError: No module named 'requests'":** `pip install requests`.
*   **"401 Unauthorized":** Неверный токен/нет прав `repo`.
*   **"422 Unprocessable Entity":** Конфликт, путь, ограничения.
*   **Не загружает подпапки:** Скрипт должен быть в *корневой* папке.
*   **Другая ветка (не `main`):** Измените `branch`.
*   **Исключить файлы/папки:**

    ```python
    if item.startswith(".") or item == "node_modules" or item.endswith(".tmp") or item in IGNORED_DIRS:
        continue
    ```

*   **Медленно:** Загрузка через API может быть медленной.

## 🚨 Ошибки и решения

| Ошибка                               | Причина                                                        | Решение                                                                              |
| :------------------------------------ | :------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| `ModuleNotFoundError: ...`          | Не установлена библиотека.                                     | `pip install <имя_библиотеки>`                                                      |
| `401 Unauthorized`                    | Неверный токен/нет прав.                                      | Проверьте токен, scope (`repo`).                                                     |
| `404 Not Found`                       | Репозиторий не найден.                                         | Проверьте номер/имя.                                                                 |
| `422 Unprocessable Entity`             | Конфликт, путь, ограничения.                                  | Проверьте путь, имя, ограничения.                                                    |
| Ошибки кодировки                       | Проблемы с символами (Windows).                               | `chcp 65001`.                                                                        |
| `Permission denied`                   | Нет прав.                                                     | Linux/macOS: `chmod +x`. Проверьте права.                                           |
| Ошибки Termux                         | Доступ к файлам.                                              | `termux-setup-storage`. SD: root?                                                    |
| **Другие ошибки**                     |                                                                | **Прочитайте сообщение**, поищите в интернете, спросите (текст, Python, ОС, действия). |
|**Неверный выбор**|Выбрано недопустимое действие|Выберите из предложенных вариантов|
|**Invalid token**|Вы ввели неверный токен , либо токен без прав|Введите корректный токен , с правами `repo`|
|**Файл {} успешно загружен/обновлен.**|Скрипт загрузил либо обновил файл|---|
|**Ошибка при загрузке файла {}: {} - {}**|При загрузке файла произошла ошибка|Проверьте подключение к интернету , попробуйте позже|
|**Invalid language choice. Using English.**|Вы ввели неверное значение для выбора языка|Выберите `en` либо `ru`|
