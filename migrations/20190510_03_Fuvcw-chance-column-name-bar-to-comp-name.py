"""
chance column name bar  to comp_name
"""

from yoyo import step

__depends__ = {'20190510_02_U9djH-add-timestamp-collumn-to-matches'}

steps = [
    step("ALTER TABLE competitors RENAME bar TO comp_name")
]
