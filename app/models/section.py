from sqlalchemy import MetaData, Table, Column, BigInteger, Integer, text, DateTime, ForeignKey, UnicodeText
from sqlalchemy.orm import relationship, backref
from app.models import Base
from app.models.paragraph import Paragraph
from db_connection import DbConnection



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
    sc_xml = Column(UnicodeText, nullable=False)
    sc_number = Column(Integer, nullable=False)
    sc_index_number = Column(Integer, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("NOW()"))
    paragraph_id = Column(BigInteger, ForeignKey("paragraph.id"))
    paragraph = relationship(Paragraph, backref=backref("sections"))


    def insert_many(self, sections):
        if sections:
            self._conn.execute(self._insert, sections)