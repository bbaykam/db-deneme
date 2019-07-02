"""
create simple score table
"""

from yoyo import step

__depends__ = {'20190530_01_4MJUA-add-alter-score-match-unique'}

steps = [
    step("CREATE TABLE score (id SERIAL, \
    player_name INT REFERENCES competitors (id),\
      result INT, set1 INT, set2 INT, set3 INT, match_date TIMESTAMP,\
      PRIMARY KEY (id))",
         "DROP TABLE score")
]
