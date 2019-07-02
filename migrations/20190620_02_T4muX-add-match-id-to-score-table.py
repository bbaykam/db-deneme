"""
add match.id to score table
"""

from yoyo import step

__depends__ = {'20190620_01_e3dU1-create-simple-score-table'}

steps = [
    step("ALTER TABLE score ADD COLUMN match_id INT REFERENCES matches (id)")
]
