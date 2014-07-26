from sqlalchemy import Table, BigInteger, Column, Unicode, Integer, UnicodeText, DateTime, text, \
    ForeignKey, MetaData
from sqlalchemy.orm import mapper

from app.models.model import Model
from db_connection import DbConnection


metadata = MetaData()

paragraph = Table("paragraph", metadata,
                  Column(BigInteger, primary_key=True),
                  Column(Unicode),
                  Column(Integer, nullable=False),
                  Column(Integer),
                  Column(UnicodeText, nullable=False),
                  Column(DateTime, nullable=False, server_default=text("NOW()")),
                  Column(BigInteger, ForeignKey("statute.id")))


class Paragraph(Model):
    def __init__(self):
        super(Paragraph, self).__init__()
        self._tbl = Table("paragraph", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()
        self._session = DbConnection().Session()

    def insert_many(self, paragraphs):
        self._conn.execute(self._insert, paragraphs)

    def get_paragraphs(self, references):
        paragraphs = []
        for ref in references:
            for paragraph in self._session.query(Paragraph).filter(Paragraph.pg_number == ref["pg_number"], Paragraph.statute_id == ref["statute_id"]).all():
                paragraphs.append(paragraph)
        return paragraphs


mapper(Paragraph, paragraph)
