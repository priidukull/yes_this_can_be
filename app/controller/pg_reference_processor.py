from app.models.paragraph import ParagraphRepo
from app.models.statute import Statute
from helpers.text_parser import TextParser


class ParagraphReferenceProcessor(object):
    def get_referred_paragraphs(self, query):
        if not query:
            return None
        statutes = Statute().get_all()
        references = TextParser().parse_pg_references(query=query, statutes=statutes)
        paragraphs = ParagraphRepo().get_paragraphs(references=references)
        return paragraphs