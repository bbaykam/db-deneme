from database import Database
from datetime import datetime
from match import Match


class Score:
    def __init__(self):
        self.db = Database()
        self.mh = Match()

    def validate(self):
        n = int(input("input set score; "))
        if 0 <= n <= 7:
            return n
        else:
            print("set value must be int and between 0 - 7 ")

    def result(self):
        result_map = {"win": 1, "lose": 2, "red": 3, "WO": 4, "delay": 5}
        try:
            result = input("match result : ")
            print(result_map[result])
            return result_map[result]
        except KeyError:
            print("chose one of 'win', 'lose', 'red', 'WO', 'delay'")

    def query_match_id(self):
        try:
            off_name = self.mh.query_comp_name_id()
            acc_name = self.mh.query_comp_name_id()
            query = ("SELECT id FROM matches \
            WHERE matches.off_name = {} and matches.acc_name = {} ORDER BY matches.match_date DESC LIMIT 1"\
                     .format(off_name, acc_name))
            query_match_id = self.db.select(query)
            print("match id; {} ".format(query_match_id))
            return self.db.select(query)
        except TypeError:
            print("Match can't find")

    def save_score(self):
        match = self.query_match_id()
        result = self.result()
        off_set1 = self.validate()
        acc_set1 = self.validate()
        off_set2 = self.validate()
        acc_set2 = self.validate()
        off_set3 = self.validate()
        acc_set3 = self.validate()
        date = input("write match date (format yyyy-mm-dd HH:MM); ")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        data = ("INSERT INTO scores \
        (match, result, off_set1, acc_set1, off_set2, acc_set2, off_set3, acc_set3, time) \
        VALUES ({}, {}, {}, {}, {}, {}, {}, {}, '{}')"\
                .format(match, result, off_set1, acc_set1, off_set2, acc_set2, off_set3, acc_set3, date))
        return self.db.query(data)


match = Score()
#match.query_match_id()
#match.validate()
match.save_score()