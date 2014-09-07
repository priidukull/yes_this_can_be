import pytest
from app.controller.pg_reference_processor import ParagraphReferenceProcessor
from app.models.paragraph import Paragraph
from app.models.section import Section
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

    def test_get_referred_paragraphs(self):
        statutes = [{"id": 44, "name": "Elektroonilise side seadus", "short_name": "ESS"}]
        Statute().insert_many(statutes=statutes)
        paragraphs = [{"id": 404, "pg_header": "Eesti raadiosagedusplaani muutmine", "pg_number": 11, "pg_xml": "<xml>Paragrahvi tekst<xml>", "statute_id": 44}]
        Paragraph().insert_many(paragraphs)
        sections = [{"id": 414, "sc_xml": "<xml>Lõike tekst</xml>", "sc_number": 1, "paragraph_id": 404}]
        Section().insert_many(sections)

        paragraphs = ParagraphReferenceProcessor().get_referred_paragraphs(query="ESS § 11")

        assert 1 == paragraphs.__len__() and 1 == paragraphs[0].sections.__len__()