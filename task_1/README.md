### Комментарии
Скрипт, который требовалось написать:

`task_1.main.script_for_task_1`

Функционал подключения к БД и обработки SQL-запросов реализован в приложении `app` 
(оно же используется и в `task_4`).
### Запуск на локальном хосте
- запуск docker-контейнеров с PostgreSQL, PGAdmin:
```bash
$ docker-compose -f task_1/docker-compose_task_1.yaml --env-file .env.example up -d
```
- запуск скрипта, который требовалось написать:
```bash
$ python3 -m task_1.main
```
Отсутствие в командной строке трассировки исключений (AssertionError и других)
говорит об успешном выполнении скрипта с тестовыми данными.
### Просмотр таблиц БД

- посмотреть таблицы БД можно в PGAdmin: http://localhost:5050/

Если откроется страница аутентификации пользователя PGAdmin, в полях для 
электронной почты и пароля нужно ввести значения переменных 
```PGADMIN_DEFAULT_EMAIL```, ```PGADMIN_DEFAULT_PASSWORD``` из файла 
```Fenster_MV/.env.example```.

### Остановка docker-контейнеров
```bash
$ docker-compose -f task_1/docker-compose_task_1.yaml down
```