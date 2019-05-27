from database import Database
from datetime import datetime

class Match:
    def __init__(self):

        self.db = Database()
        self.table = 'matches'

    def validate(self, data):
        pass

    def query_comp_name_id(self, name):
        try:
            name = input("write competitor name : ")
            query = ("SELECT id FROM competitors WHERE comp_name = '{}'".format(name))
            comp_name_id = self.db.select(query)
            print("competitor name  id; {} ".format(comp_name_id))
            return self.db.select(query)
        except TypeError:
            print("competitor '{}' can't find".format(name))

    def result(self, result):
        result_map = {"win": 1, "lose": 2, "red": 3, "WO": 4, "delay": 5}
        try:
            result = input("match result : ")
            print(result_map[result])
            return result_map[result]
        except KeyError:
            print("chose one of 'win', 'lose', 'red', 'WO', 'delay'")

    def save_match(self, off_name, acc_name, result, date):
        off_name = self.query_comp_name_id(off_name)
        acc_name = self.query_comp_name_id(acc_name)
        result = self.result(result)
        date = input("write match date (format yyyy-mm-dd HH:MM); ")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        data = ("INSERT INTO matches (off_name, acc_name, result, match_date) VALUES ({}, {}, {}, '{}')".format(off_name, acc_name, result, date))
        print(data)
        return self.db.query(data)



player = Match()
#player.query_comp_name_id('ayse')
#player.result('win')
player.save_match(24, 25, 4, "")