import os

from dotenv import load_dotenv


if os.getenv('DOCKER') is not None:
    load_dotenv('.env')
else:
    load_dotenv('.env.dev')

config = {
    "postgres_user": os.getenv("POSTGRES_USER"),
    "postgres_password": os.getenv("POSTGRES_PASSWORD"),
    "postgres_db": os.getenv("POSTGRES_DB"),
    "postgres_host": os.getenv("POSTGRES_HOST"),
    "postgres_port": os.getenv("POSTGRES_PORT")
}