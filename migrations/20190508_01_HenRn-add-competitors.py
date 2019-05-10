"""
Add competitors
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE competitors (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
        "DROP TABLE competitors")
]
