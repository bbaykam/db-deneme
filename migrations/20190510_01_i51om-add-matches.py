"""
Add matches
"""

from yoyo import step

__depends__ = {'20190508_01_HenRn-add-competitors'}

steps = [
    step("CREATE TABLE matches (id SERIAL, \
    off_name INT REFERENCES competitors (id),\
     acc_name INT REFERENCES competitors (id),\
      result INT, off_set_1 int, acc_net_1 int, \
       tiebreak int, PRIMARY KEY (id))",
         "DROP TABLE matches")
]
