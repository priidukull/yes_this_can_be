import pytest
from sqlalchemy import select, MetaData, ForeignKeyConstraint, Table
from sqlalchemy.engine import reflection
from sqlalchemy.sql.ddl import DropConstraint

from app.models.model import Model
from app.models.statute import Statute
from app.models.statute_xml import StatuteXml
from test.test_models.prepations import DB

class DB(DB):
    def begin(self, name):
        self.intransaction.append(name)
        Statute().insert_many(statutes=[{"id": 1, "name": "foo", "short_name": "f"},
                                        {"id": 2, "name": "bar", "short_name": "b"}])
        if "get_by_statute_ids" in name:
            StatuteXml().insert(url="url_foo", xml="xml_foo", statute_id=1)
            StatuteXml().insert(url="url_bar", xml="xml_foo", statute_id=2)


@pytest.fixture(scope="module")
def db():
    return DB()

class TestClass(object):
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        request.addfinalizer(db.rollback)

    def test_insert(self):
        StatuteXml().insert(url="url_foo", xml="xml_foo", statute_id=1)

        actual = Model()._conn.execute(select([StatuteXml()._tbl])).fetchone()
        assert actual

    def test_get_by_statute_ids(self):
        actual = StatuteXml().get_by_statute_ids(statute_ids=[1])

        assert 1 == len(actual)

    def test_get_by_statute_ids_when_no_statute_ids_are_given(self):
        actual = StatuteXml().get_by_statute_ids()

        assert 2 == len(actual)