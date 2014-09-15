import pytest
from app.models.statute import Statute
from deriving.derive_paragraphs import DeriveParagraphs
from test.test_models.prepations import DB
from singletons import DbConnection


@pytest.fixture(scope="class")
def db():
    return DB()

class TestClass(object):
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        request.addfinalizer(db.rollback)

    def test_derive_one(self):
        statutes = [{"id": 1, "name": "foo", "short_name": "bar"}]
        Statute().insert_many(statutes=statutes)
        row = {"statute_id": 1, "xml": """
        <paragrahv id="para1">
            <kuvatavNr><![CDATA[§ 1. ]]></kuvatavNr>
        </paragrahv>
        <paragrahv id="para2">
            <kuvatavNr><![CDATA[§ 1<sup>1</sup>.]]></kuvatavNr>
        </paragrahv>"""}

        DeriveParagraphs()._derive_one(row=row)

        actual = DbConnection().engine.execute("SELECT count(*) FROM paragraph").scalar()
        assert 2 == actual
