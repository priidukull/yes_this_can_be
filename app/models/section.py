from sqlalchemy import MetaData, Table, select
from app.models.models import Section
from singletons import DbConnection


class SectionRepo(Section):
    def __init__(self):
        super(SectionRepo, self).__init__()
        self._metadata = MetaData()
        self._engine = DbConnection().engine
        self._conn = DbConnection().conn
        self._tbl = Table("section", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()

    def insert_many(self, sections):
        if sections:
            self._conn.execute(self._insert, sections)

    def get_all(self, section_ids=None):
        query = select([self._tbl])
        if section_ids:
            query = query.where(self._tbl.c.id.in_(section_ids))
        return self._engine.execute(query).fetchall()