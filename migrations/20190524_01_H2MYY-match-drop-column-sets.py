"""
match drop column sets 
"""

from yoyo import step

__depends__ = {'20190520_01_8VtKh-alter-date-to-datetime'}

steps = [
    step("ALTER TABLE matches DROP COLUMN off_set_1, DROP COLUMN acc_net_1, DROP COLUMN tiebreak")
]
