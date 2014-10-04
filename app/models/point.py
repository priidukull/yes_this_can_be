from sqlalchemy import MetaData, Table
from app.models.models import Point
from singletons import DbConnection


class PointRepo(Point):
  def __init__(self):
    super(PointRepo, self).__init__()
    self._metadata = MetaData()
    self._engine = DbConnection().engine
    self._conn = DbConnection().conn
    self._tbl = Table("point", self._metadata, autoload=True, autoload_with=self._engine)
    self._insert = self._tbl.insert()

  def insert_many(self, points):
    if points:
      self._conn.execute(self._insert, points)

