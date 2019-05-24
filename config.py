import configparser


class Config:
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)

    def get(self, key):
        return self.config['default'][key]
