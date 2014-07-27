from sqlalchemy import Table, select, func, MetaData
from db_connection import DbConnection


class Statute(object):
    def __init__(self):
        super(Statute, self).__init__()
        self._metadata = MetaData()
        self._engine = DbConnection().engine
        self._conn = DbConnection().conn
        self._tbl = Table("statute", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()

    def insert_many(self, statutes):
        return self._conn.execute(self._insert, statutes)

    def get_statute(self, query):
        query = query.lower()
        sql = select([self._tbl]).where(func.lower(self._tbl.c.short_name) == query)
        return self._engine.execute(sql).fetchone()


