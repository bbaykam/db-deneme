"""
add score table 
"""

from yoyo import step

__depends__ = {'20190524_02_ot6Nz-add-colum-timestamp-to-match'}

steps = [
    step("CREATE TABLE scores (id SERIAL, \
    match INT REFERENCES matches (id),\
      result INT, off_set1 INT, acc_set1 INT, \
      off_set2 INT, acc_set2 INT, off_set3 INT, acc_set3 INT,\
       time TIMESTAMP, PRIMARY KEY (id))",
         "DROP TABLE scores")
]
