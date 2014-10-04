import pytest

from app.models.statute import Statute
from test.test_models.prepations import DB


class DB(DB):
  def begin(self, name):
    self.intransaction.append(name)
    if "mixed_case" in name:
      statutes = [{"name": "nAmE of statute one", "short_name": "nAmE1"},
                  {"name": "nAmE of statute two", "short_name": "nAmE2"}]
    else:
      statutes = [{"name": "name of statute one", "short_name": "name1"},
                  {"name": "name of statute two", "short_name": "name2"}]
    Statute().insert_many(statutes=statutes)


@pytest.fixture(scope="class")
def db():
  return DB()


class TestClass(object):
  @pytest.fixture(autouse=True)
  def transact(self, request, db):
    db.begin(request.function.__name__)
    request.addfinalizer(db.rollback)

  def test_get_all(self):
    expected = 2

    actual = Statute().get_all().__len__()

    assert expected == actual

  def test_get_statute_by_short_name(self):
    actual = Statute().get_statute(query="name1")

    assert "name of statute one" == actual["name"]

  def test_get_statute_by_short_name_when_case_does_not_match(self):
    actual = Statute().get_statute(query="nAmE1")

    assert "name of statute one" == actual["name"]

  def test_get_statute_by_short_name_when_short_name_in_db_is_in_mixed_case(self):
    actual = Statute().get_statute(query="nAmE1")

    assert "name of statute one" == actual["name"].lower()
