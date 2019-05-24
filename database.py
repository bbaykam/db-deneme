import psycopg2
from config import Config


class Database:
    def __init__(self):
        self.config = Config('database.ini')
        self.conn = psycopg2.connect(host=self.config.get('host'), \
                                    dbname=self.config.get('dbname'), \
                                    user=self.config.get('user'), \
                                    password=self.config.get('password'))
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        return self.conn.commit()

    def select(self, table, fields=[]):
        query = "SELECT {} FROM {};".format(table, fields.join(','))
        self.cur.execute(query)
        self.cur.close()

    def insert(self, table, column, data):
        self.query = ("INSERT INTO {} ({}) VALUES ('{}')".format(table, column, data))
        return self.query

#player = Database()
#player.query_comp_name_id('ayse')
#player.insert_match('abbas', 'cemal', '', 1, 6, 1, '2019-05-01 14:30')
#player.insert_name('competitor')
#player.result('')