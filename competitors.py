import  psycopg2
from database import Database

class Competitor:
    def __init__(self, competitor_data={}):
        self.data = competitor_data
        self.db = Database()

    def save(self, data):
        return self.db.insert(data)
