"""
Alter date to datetime 
"""

from yoyo import step

__depends__ = {'20190513_01_RFKRu-set-serial-id-table-competitors'}

steps = [
    step("ALTER TABLE matches ALTER COLUMN match_date TYPE timestamp")
]
