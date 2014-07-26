from sqlalchemy import Table, select

from app.models.model import Model


class StatuteXml(Model):
    def __init__(self):
        super(StatuteXml, self).__init__()
        self._tbl = Table("statute_xml", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()

    def insert(self, url, xml, statute_id):
        params = self._insert.values(url=url, xml=xml, statute_id=statute_id).compile().params
        self._conn.execute(self._insert, params)

    def get_by_statute_ids(self, statute_ids=None):
        try:
            query = select([self._tbl]).where(self._tbl.c.statute_id.in_(statute_ids))
            return self._conn.execute(query).fetchall()
        except TypeError:
            return self.get_all()