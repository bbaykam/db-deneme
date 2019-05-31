from database import Database

class Competitor:
    def __init__(self, competitor_name={}):
        self.data = competitor_name
        self.db = Database()

    def validate(self, data):
        pass

    def save(self):
        name = input("Input competitor name; ")
        data = ("INSERT INTO competitors (comp_name) VALUES ('{}')".format(name))
        print(data)
        return self.db.query(data)




player = Competitor()
player.save()