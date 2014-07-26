from sqlalchemy import create_engine, MetaData, select
from app import db, app
import config


class Model(object):
    def __init__(self):
        self._engine = db.get_engine(app=app)
        self._conn = self._engine.connect()
        self._metadata = MetaData()

    def get_all(self):
        s = select([self._tbl])
        rows = self._conn.execute(s).fetchall()
        return rows