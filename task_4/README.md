### Запуск и остановка на локальном хосте
- #### запуск docker-контейнеров с PostgreSQL, DBAdmin:
```bash
$ cd task_4
$ docker compose -f docker-compose_task_4.yaml up -d
```
- #### запуск скрипта, который требовалось написать:
```bash
$ cd python3 main.py  # из директории /task_4
```
- #### остановка контейнеров:
```bash
$ docker-compose -f docker-compose_task_4.yaml down
```