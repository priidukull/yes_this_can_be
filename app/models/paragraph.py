from flask import logging
from sqlalchemy import Table, MetaData, select
from app.models.models import Paragraph
from singletons import DbConnection



class ParagraphRepo(Paragraph):
    def __init__(self):
        super(ParagraphRepo, self).__init__()
        self._metadata = MetaData()
        self._engine = DbConnection().engine
        self._conn = DbConnection().conn
        self._tbl = Table("paragraph", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()
        self._session = DbConnection().Session()

    def insert_many(self, paragraphs):
        for pg in paragraphs:
            self._conn.execute(self._insert, [pg])

    def get_paragraphs(self, references):
        paragraphs = []
        for ref in references:
            pg = self._session.query(ParagraphRepo).filter(ParagraphRepo.pg_number == ref["pg_number"], ParagraphRepo.statute_id == ref["statute_id"]).first()
            paragraphs.append(pg)
        return paragraphs

    def get_all(self, paragraph_ids):
        query = select([self._tbl])
        if paragraph_ids:
            query = query.where(self._tbl.c.paragraph_id.in_(paragraph_ids))
        return self._engine.execute(query).fetchall()