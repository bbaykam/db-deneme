import psycopg2
from config import Config


class Database:
    def __init__(self):
        config = Config('default.ini')
        connection = config.get('db_host')

    def insert(self, table, data):
        pass

    def select(self, table, fields=[]):
        pass

