"""
SET SERIAL ID table competitors
"""

from yoyo import step

__depends__ = {'20190510_03_Fuvcw-chance-column-name-bar-to-comp-name'}

steps = [
    step("CREATE SEQUENCE competitors_id_seq"),
    step("ALTER TABLE competitors ALTER COLUMN id SET DEFAULT nextval('competitors_id_seq')")
]