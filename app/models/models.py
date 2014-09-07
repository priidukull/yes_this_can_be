from sqlalchemy import Column, BigInteger, Unicode, Integer, UnicodeText, DateTime, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Paragraph(Base):
    __tablename__ = "paragraph"
    id = Column(BigInteger, primary_key=True)
    pg_header = Column(Unicode)
    pg_number = Column(Integer, nullable=False)
    pg_index_number = Column(Integer)
    pg_xml = Column(UnicodeText, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("NOW()"))
    statute_id = Column(BigInteger, ForeignKey("statute.id"))
    sections = relationship("Section", backref="paragraph")


class Section(Base):
    __tablename__ = "section"
    id = Column(BigInteger, primary_key=True)
    sc_xml = Column(UnicodeText, nullable=False)
    sc_number = Column(Integer, nullable=False)
    sc_index_number = Column(Integer, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("NOW()"))
    paragraph_id = Column(BigInteger, ForeignKey("paragraph.id"))