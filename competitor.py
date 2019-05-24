from database import Database
import psycopg2

class Competitor:
    def __init__(self, competitor_name={}):
        self.data = competitor_name
        self.db = Database()
        self.table = 'competitors'
        self.column = 'comp_name'

    def validate(self, data):
        pass


    def save(self, data):
        data = input("Input competitor name; ")
        data = self.db.insert(self.table, self.column, data)
        print(data)

        return self.db.query(data)




player = Competitor()
player.save('')