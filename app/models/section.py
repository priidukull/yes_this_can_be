from sqlalchemy import MetaData, Table, Column, BigInteger, Integer, text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db_connection import DbConnection


Base = declarative_base()

class Section(Base):
    def __init__(self):
        super(Section, self).__init__()
        self._metadata = MetaData()
        self._engine = DbConnection().engine
        self._conn = DbConnection().conn
        self._tbl = Table("section", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()

    __tablename__ = "section"
    id = Column(BigInteger, primary_key=True)
    sc_number = Column(Integer, nullable=False)
    sc_index_number = Column(Integer, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("NOW()"))
    paragraph = Column(BigInteger, ForeignKey("paragraph.id"))

    def insert_many(self, sections):
        self._conn.execute(self._insert, sections)