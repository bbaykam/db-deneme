import psycopg2
from database import Database

class Match:
    def __init__(self, off_name, acc_name, result, off_set_1, acc_set_1, tiebreak, match_date):
        self.off = off_name
        self.acc = acc_name
        self.r = result
        self.off1 = off_set_1
        self. acc1 = acc_set_1
        self.tie = tiebreak
        self.date = match_date


    def result(self):
        result = input("match result : ")
        result_map = {"win": 1, "lose": 2, "red": 3, "WO": 4, "delay": 5}

        return result_map[result]

    def save(self):
        """ insert match name into the matches table  """

        conn = Connect.connect_db()
        try:

            # create a new cursor# execute the INSERT statement
            cur = conn.cursor
            cur.execute("INSERT INTO matches (off_name, acc_name, result, off_set_1, acc_set_1, tiebreak, match_date ) VALUES (self.off, self.acc, self.r, self.off1, self.acc1, self.tie,  self.date)")
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


self.db.insert(data)
