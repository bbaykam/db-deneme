from database import Database
from datetime import datetime

class Match:
    def __init__(self):

        self.db = Database()
        self.table = 'matches'

    def validate(self, data):
        pass

    def query_comp_name_id(self):
        try:
            name = input("write competitor name : ")
            query = ("SELECT id FROM competitors WHERE comp_name = '{}' LIMIT 1".format(name))
            comp_name_id = self.db.select(query)
            print("competitor name  id; {} ".format(comp_name_id))
            return self.db.select(query)
        except TypeError:
            print("competitor '{}' can't find".format(name))

    def status(self):
        status_map = {"ok": 1, "red": 2}
        try:
            status = input("match STATUS : ")
            print(status_map[status])
            return status_map[status]
        except KeyError:
            print("chose one of 'ok', 'red'")

    def save_match(self):
        off_name = self.query_comp_name_id()
        acc_name = self.query_comp_name_id()
        status = self.status()
        date = input("write match date (format yyyy-mm-dd HH:MM); ")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        data = ("INSERT INTO matches (off_name, acc_name, result, match_date) VALUES ({}, {}, {}, '{}')" \
                .format(off_name, acc_name, status, date))
        print(data)
        return self.db.query(data)



player = Match()
#player.query_comp_name_id()
#player.result('win')
#player.save_match()