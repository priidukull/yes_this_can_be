from sqlalchemy import Table, MetaData, select
from app.models.models import Paragraph
from singletons import DbConnection



class ParagraphRepo(Paragraph):
    def __init__(self):
        super(ParagraphRepo, self).__init__()
        self._metadata = MetaData()
        self._engine = DbConnection().engine
        self._conn = DbConnection().conn
        self._tbl = Table("paragraph", self._metadata, autoload=True, autoload_with=self._engine)
        self._insert = self._tbl.insert()
        self._session = DbConnection().Session()

    def insert_many(self, paragraphs):
        self._conn.execute(self._insert, paragraphs)

    def get_paragraphs(self, references):
        paragraphs = []
        for ref in references:
            pgs = self._session.query(ParagraphRepo).filter(ParagraphRepo.pg_number == ref["pg_number"], ParagraphRepo.statute_id == ref["statute_id"]).all()
            if len(pgs) > 1:
                raise Exception("Too many paragraphs correspond to that query.")
            if len(pgs) == 1:
                paragraphs.append(pgs[0])
        return paragraphs

    def get_all(self):
        query = select([self._tbl])
        return self._engine.execute(query).fetchall()