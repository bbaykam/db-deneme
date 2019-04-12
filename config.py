from configparser import ConfigParser


class Config:
    def config(filename ='database.ini', section = 'postgresql'):
        parser = ConfigParser()
        parser.read("mydb")

