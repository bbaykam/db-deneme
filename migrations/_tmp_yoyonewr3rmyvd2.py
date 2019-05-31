"""
add ALTER competitors.comp_name unique
"""

from yoyo import step

__depends__ = {'20190530_01_4MJUA-add-alter-score-match-unique'}

steps = [
    step("ALTER TABLE competitors ADD UNIQUE (comp_name)")
]
