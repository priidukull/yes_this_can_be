from sqlalchemy import Table, BigInteger, Column, Unicode, Integer, UnicodeText, DateTime, text, \
    ForeignKey, MetaData, select
from app.models import Base
from db_connection import DbConnection



class Paragraph(Base):
    def __init__(self):
        super(Paragraph, self).__init__()
        self._metadata = MetaData()
        self._engine = DbConnection().engine
        self._conn = DbConnection().conn
        self._tbl = Table("paragraph", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()
        self._session = DbConnection().Session()

    __tablename__ = "paragraph"
    id = Column(BigInteger, primary_key=True)
    pg_header = Column(Unicode)
    pg_number = Column(Integer, nullable=False)
    pg_index_number = Column(Integer)
    pg_xml = Column(UnicodeText, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("NOW()"))
    statute_id = Column(BigInteger, ForeignKey("statute.id"))

    def insert_many(self, paragraphs):
        self._conn.execute(self._insert, paragraphs)

    def get_paragraphs(self, references):
        paragraphs = []
        for ref in references:
            pgs = self._session.query(Paragraph).filter(Paragraph.pg_number == ref["pg_number"], Paragraph.statute_id == ref["statute_id"]).all()
            if len(pgs) > 1:
                raise Exception("Too many paragraphs correspond to that query.")
            if len(pgs) == 1:
                paragraphs.append(pgs[0])
        return paragraphs

    def get_all(self):
        query = select([self._tbl])
        return self._engine.execute(query).fetchall()