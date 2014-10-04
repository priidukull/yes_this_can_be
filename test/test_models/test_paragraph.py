import pytest

from app.models.paragraph import ParagraphRepo
from app.models.statute import Statute
from test.test_models.prepations import DB


class DbParagraphs(DB):
  def begin(self, name):
    self._paragraph_mdl = ParagraphRepo()
    self.intransaction.append(name)
    statutes = [{"id": 44, "name": "Elektroonilise side seadus", "short_name": "ESS"}]
    Statute().insert_many(statutes=statutes)
    paragraphs = [{"pg_header": "Eesti raadiosagedusplaani muutmine", "pg_number": 11, "pg_xml": "<xml>Paragrahvi tekst<xml>", "statute_id": 44}]
    self._paragraph_mdl.insert_many(paragraphs)


@pytest.fixture(scope="class")
def db():
  return DbParagraphs()


class TestClass(object):
  @pytest.fixture(autouse=True)
  def transact(self, request, db):
    db.begin(request.function.__name__)
    request.addfinalizer(db.rollback)

  def setup(self):
    self._paragraph_mdl = ParagraphRepo()

  def test_get_paragraphs_from_two_pg_numbers(self):
    actual = self._paragraph_mdl.get_paragraphs([{"statute_id": 44, "pg_number": 11}])

    assert 11 == actual[0].pg_number

  def test_paragraphs_from_two_statute_ids(self):
    statutes = [{"id": 43, "name": "foo", "short_name": "f"}]
    Statute().insert_many(statutes=statutes)
    paragraphs = [{"pg_header": "foobar", "pg_number": 11, "pg_xml": "<xml>foobar<xml>", "statute_id": 43}]
    self._paragraph_mdl.insert_many(paragraphs)

    actual = self._paragraph_mdl.get_paragraphs([{"statute_id": 43, "pg_number": 11}])

    assert 11 == actual[0].pg_number and 43 == actual[0].statute_id

  def test_get_paragraphs_from_two_statute_ids_when_there_are_more_than_one_reference(self):
    paragraphs = [{"pg_header": "foobar", "pg_number": 12, "pg_xml": "<xml>foobar<xml>", "statute_id": 44}]
    self._paragraph_mdl.insert_many(paragraphs)

    actual = self._paragraph_mdl.get_paragraphs([{"statute_id": 44,
                                                  "pg_number": 11},
                                                 {"statute_id": 44,
                                                  "pg_number": 12}])

    assert 2 == len(actual)

  def test_get_paragraphs_when_paragraph_does_not_exist(self):
    references = [{'pg_number': 12, 'statute_id': 44}]

    actual = self._paragraph_mdl.get_paragraphs(references=references)

    assert [] == actual