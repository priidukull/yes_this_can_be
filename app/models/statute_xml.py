from sqlalchemy import Table, select, MetaData
from singletons import DbConnection


class StatuteXml(object):
  def __init__(self):
    super(StatuteXml, self).__init__()
    self._meta = MetaData()
    self._engine = DbConnection().engine
    self._tbl = Table("statute_xml", self._meta, autoload=True, autoload_with=self._engine)
    self._insert = self._tbl.insert()

  def insert(self, url, xml, statute_id):
    params = self._insert.values(url=url, xml=xml, statute_id=statute_id).compile().params
    self._engine.execute(self._insert, params)

  def get_by_statute_ids(self, statute_ids=None):
    try:
      query = select([self._tbl]).where(self._tbl.c.statute_id.in_(statute_ids))
      return self._engine.execute(query).fetchall()
    except TypeError:
      return self._engine.execute(select([self._tbl])).fetchall()