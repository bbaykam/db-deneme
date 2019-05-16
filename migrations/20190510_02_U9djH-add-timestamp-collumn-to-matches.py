"""
Add timestamp collumn to matches
"""

from yoyo import step

__depends__ = {'20190510_01_i51om-add-matches'}

steps = [
    step("ALTER TABLE matches ADD COLUMN match_date DATE NOT NULL ")
]
