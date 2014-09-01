import pytest
from app.controller.pg_reference_processor import ParagraphReferenceProcessor
from test.test_models.test_paragraph import DbParagraphs


@pytest.fixture(scope="class")
def db():
    return DbParagraphs()

class TestClass(object):
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        request.addfinalizer(db.rollback)

    def test_get_referred_paragraphs(self):
        paragraphs = ParagraphReferenceProcessor().get_referred_paragraphs(query="ESS § 11")

        assert 1 == paragraphs.__len__()