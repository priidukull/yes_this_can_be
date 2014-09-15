import argparse
import logging
from app.models import statute_xml
from deriving.derive_points import DerivePoints
from deriving.derive_sections import DeriveSections
from helpers import statute_xml_helper
from app.models.paragraph import ParagraphRepo


class DeriveParagraphs():
    def __init__(self):
        self._paragraph_mdl = ParagraphRepo()
        self._statute_xml_helper = statute_xml_helper.Helper()
        self._statute_xml_mdl = statute_xml.StatuteXml()

    def derive_all(self, statute_ids=None):
        logging.info("Started deriving paragraphs")
        rows = self._statute_xml_mdl.get_by_statute_ids(statute_ids=statute_ids)
        for row in rows:
            self._derive_one(row)
            logging.info("COMPLETED deriving paragraphs")

    def _derive_one(self, row):
        paragraphs = self._statute_xml_helper.parse_paragraphs(row=row)
        self._paragraph_mdl.insert_many(paragraphs=paragraphs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Derives paragraphs and may be other features')
    parser.add_argument('--dep', help='also derive depending features', dest='dep', action='store_true')
    parser.add_argument('-id', metavar='statute_id', type=int, nargs='+', help='ids of the statutes for which paragraphs are to be derived')

    args = parser.parse_args()
    if hasattr(args, 'id') and args.id:
        DeriveParagraphs().derive_all(statute_ids=args.id)
    else:
        DeriveParagraphs().derive_all()
    if hasattr(args, 'dep') and args.dep:
        DeriveSections().derive_all()
        DerivePoints().derive_all()





