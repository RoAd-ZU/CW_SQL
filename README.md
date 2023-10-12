# -
В данном проекте в файле `"sql.py"` производятся `создание базы данных "cw5"` и `создание таблиц` в ней, а так же 
заполнение этих таблиц данными из https://api.hh.ru/, посредством работы с классами в файле `"get_api.py"`.
# -
После создания и заполнения таблиц производится работа с данными из базы данных "cw5" на основе ответов пользователя.

# Для запуска проекта необходимо: 
- что бы на компьютере была установленна postgresql с локальной БД;
- установить зависимости через терминал командой `pip install -r requirements.txt`;
- ~~перевести 150000 руб. мне на карту~~ не удержался :grin:

При запуске main будет запрошен пароль пользователя "postgres". Если база данных "cw5" уже существует, программа 
известит и перейдёт сразу к работе с данными в таблицах cw5.
