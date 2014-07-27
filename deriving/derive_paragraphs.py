from app.models import statute_xml
from helpers import statute_xml_helper
from app.models.paragraph import Paragraph


class DeriveParagraphs(object):
    def __init__(self):
        self._statute_xml_mdl = statute_xml.StatuteXml()
        self._statute_xml_helper = statute_xml_helper.Helper()

    def derive_all(self, statute_ids=None):
        rows = self._statute_xml_mdl.get_by_statute_ids(statute_ids=statute_ids)
        for row in rows:
            paragraphs = self._statute_xml_helper.parse_paragraphs(row=row)
            Paragraph().insert_many(paragraphs=paragraphs)



if __name__ == "__main__":
    DeriveParagraphs().derive_all()
