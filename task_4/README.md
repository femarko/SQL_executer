### Комментарии
Скрипт, который требовалось написать:

`task_4.main.script_for_task_4`

Функционал подключения к БД и обработки SQL-запросов реализован в приложении `app` 
(оно также используется в `task_1` и в `task_7`).\
"Сырой" SQL импортируется в `task_4.main` из `task_4.input_sql_statements`.
### Запуск на локальном хосте
*Все команды выполняются из корневой директории проекта*
- запуск docker-контейнеров с PostgreSQL, PGAdmin:
```bash
$ docker-compose -f task_4/docker-compose_task_4.yaml up -d
```
- запуск скрипта, который требовалось написать:
```bash
$ python3 -m task_4.main
```
Отсутствие в командной строке трассировки исключений (AssertionError и других)
говорит об успешном выполнении скрипта с тестовыми данными.
### Просмотр таблиц БД

- ссылка для просмотра таблиц БД: http://localhost:5050/
- если откроется страница аутентификации пользователя PGAdmin:
  - в полях для электронной почты и пароля нужно ввести значения переменных 
  ```PGADMIN_DEFAULT_EMAIL```, ```PGADMIN_DEFAULT_PASSWORD``` из файла ```task_4/.env.example```
  - после входа в систему во всплывающем окне Set Master Password нужно установить пароль по 
  собственному усмотрению и в разделе Quick Links выбрать Add New Server
  - в открывшемся окне в поле Name ввести название соединения по собственному усмотрению
  - перейти на вкладку Connection, в которой:
    - в поле Host name/address, ввести значение переменной ```POSTGRES_HOST``` из файла 
    ```task_1/.env.example```
    - в поле Port ввести: 5432,
    - в полях Maintenance database, Username, Password ввести: postgres.
### Остановка docker-контейнеров
```bash
$ docker-compose -f task_4/docker-compose_task_4.yaml down
```