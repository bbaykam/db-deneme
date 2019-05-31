"""
add ALTER score.match UNIQUE
"""

from yoyo import step

__depends__ = {'20190527_01_9X7OR-add-score-table'}

steps = [
    step("ALTER TABLE scores ADD UNIQUE (match)")
]
