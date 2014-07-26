from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import config


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DbConnection(metaclass=Singleton):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object('config')
        self.db = SQLAlchemy(self.app)
        self.engine = self.db.create_engine(config.SQLALCHEMY_DATABASE_URI)
        self.conn = self.engine.connect()
        self.Session = sessionmaker(bind=self.engine)