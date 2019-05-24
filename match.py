from database import Database
from datetime import datetime

class Match:
    def __init__(self, competitor_name={}):
        self.data = competitor_name
        self.db = Database()
        self.table = 'matches'

    def validate(self, data):
        pass

    def query_comp_name_id(self, query):
        try:
            query = input("write competitor name : ")
            self.cur.execute("SELECT id FROM competitors WHERE comp_name = %s", (query,))
            comp_name_id = self.cur.fetchone()[0]
            print(comp_name_id)
            return self.comp_name_id()
        except TypeError:
            print("competitor '{}' can't find".format(query))

    def result(self, result):
        result_map = {"win": 1, "lose": 2, "red": 3, "WO": 4, "delay": 5}
        try:
            result = input("match result : ")
            print(result_map[result])
            return result_map[result]
        except KeyError:
            print("chose one of 'win', 'lose', 'red', 'WO', 'delay'")

    def insert_match(self, off_name, acc_name, result, off_set_1, acc_set_1, tiebreak, date):
        off_name = self.query_comp_name_id(off_name)
        acc_name = self.query_comp_name_id(acc_name)
        result = self.result(result)
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        self.cur.execute("INSERT INTO matches \
                   (off_name, acc_name, result, off_set_1, acc_net_1, tiebreak, match_date) \
                   VALUES (%s, %s, %s, %s, %s, %s, %s);",
                         (off_name, acc_name, result, off_set_1, acc_set_1, tiebreak, date))



    def save(self, data):
        return self.db.query(data)


