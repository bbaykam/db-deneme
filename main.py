from config import Config
from database import Database
from transform import Transform

config = Config()
db = Database(config)
tr = Transform(db)
