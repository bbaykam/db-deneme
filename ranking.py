from database import Database


class Ranking:
    def __init__(self):
        self.db = Database()


    def query_ranking(self):
        query = ("select ROW_NUMBER() OVER (ORDER BY sum desc nulls last) \
                    as rank, competitors.comp_name, sum from \
                    (select c.comp_name, sum(s.set1 + s.set2 + s.set3) filter \
                    (where s.match_date > current_date - interval '3' month) \
                    from competitors as c left join score as s on c.id= s.player_name \
                    group by c.comp_name  LIMIT 128) competitors;")
        for i in self.db.select_all(query):
            print(i)
        print("World no 3:", self.db.select_all(query)[2][1])
        return self.db.select_all(query)

player = Ranking()
player.query_ranking()


