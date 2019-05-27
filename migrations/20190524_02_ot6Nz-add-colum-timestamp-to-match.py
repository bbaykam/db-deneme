"""
add colum timestamp to match 
"""

from yoyo import step

__depends__ = {'20190524_01_H2MYY-match-drop-column-sets'}

steps = [
    step("ALTER TABLE matches ADD COLUMN time TIMESTAMP  DEFAULT NOW()")
]
