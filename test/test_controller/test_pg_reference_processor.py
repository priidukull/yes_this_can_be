import pytest
from app.controller.pg_reference_processor import ParagraphReferenceProcessor
from app.models.paragraph import ParagraphRepo
from app.models.section import SectionRepo
from app.models.statute import Statute
from test.test_models.prepations import DB
from test.test_models.test_paragraph import DbParagraphs


@pytest.fixture(scope="class")
def db():
  return DB()


class TestClass(object):
  @pytest.fixture(autouse=True)
  def transact(self, request, db):
    db.begin(request.function.__name__)
    request.addfinalizer(db.rollback)

  def setup(cls):
    statutes = [{"id": 44, "name": "Elektroonilise side seadus", "short_name": "ESS"}]
    Statute().insert_many(statutes=statutes)
    paragraphs = [{"id": 404,
                   "pg_header": "Eesti raadiosagedusplaani muutmine",
                   "pg_number": 11,
                   "pg_xml": "<xml>Paragrahvi tekst<xml>",
                   "statute_id": 44}]
    ParagraphRepo().insert_many(paragraphs)
    sections = [{"id": 414, "sc_xml": "<xml>Lõike tekst</xml>", "sc_number": 1, "paragraph_id": 404}]
    SectionRepo().insert_many(sections)

  def test_get_referred_paragraphs(self):
    actual = ParagraphReferenceProcessor().get_referred_paragraphs(query="ESS § 11")

    assert 1 == actual.__len__() and 1 == actual[0].sections.__len__()

  def test_get_referred_paragraphs_when_pg_does_not_exit(self):
    actual = ParagraphReferenceProcessor().get_referred_paragraphs(query="ESS § 12")

    assert [] == actual