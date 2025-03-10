import psycopg2

from task_1.app.config import config


pspg2_conn = psycopg2.connect(
    host=config["postgres_host"],
    port=config["postgres_port"],
    dbname=config["postgres_db"],
    user=config["postgres_user"],
    password=config["postgres_password"]
)


