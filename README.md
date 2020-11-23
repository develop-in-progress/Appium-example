# Пример тестового фреймворка на Аппиуме
### Тестовый фреймворк для приложения Википедии, тестирование поиска, смены языка, скрытия/восстановления статьи на Abdroid и iOS
1.  Клонируйте проект с GitHub и активируйте виртуальное окружение:
    ##### `python -m venv selenium_env`
    For Win:
    ##### `selenium_env\Scripts\activate.bat`
    For Unix:
    ##### `source selenium_env/Scripts/activate`
    Не сработает - запустите через sudo, или откройте проект в PyCharm, он поднимет venv с колен самостоятельно)# Appium-example
2.  Для запуска вам потребуется актуальная версия Питона, Аппиума и PyTest
    Установка зависимостей (при наличии [Python](https://www.python.org/)) через терминал:
    ##### `pip install -r requirements.txt`
3.  Общий тест запускается командой (терминал открыт в папке проекта, по умолчанию тест бежит для Андроида на виртуальной машине локально, нужен открытый эмулятор девайса):
    ##### `pytest`
    Смена эмулятора на iOS
    ##### `pytest --platform=ios_emulator_local`
    Выполнение удаленно на saucelabs для Android [нужно прописать имя и пароль](https://wiki.saucelabs.com/display/DOCS/Best+Practice%3A+Use+Environment+Variables+for+Authentication+Credentials)
    ##### `>pytest --platform=android_saucelab_emulator`
    Выполнение удаленно на saucelabs для iOS
    ##### `pytest --platform=ios_saucelab_emulator`