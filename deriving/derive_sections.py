import argparse
import logging
from app.models.paragraph import ParagraphRepo
from app.models.section import SectionRepo
from helpers.paragraph_helper import Helper


class DeriveSections():
    def __init__(self):
        self._paragraph_helper = Helper()
        self._paragraph_repo = ParagraphRepo()
        self._section_repo = SectionRepo()

    def derive_all(self, paragraph_ids=None):
        logging.info("COMPLETED deriving sections")
        paragraphs = self._paragraph_repo.get_all(paragraph_ids=paragraph_ids)
        for row in paragraphs:
            sections = self._paragraph_helper.parse_sections(row=row)
            self._section_repo.insert_many(sections=sections)
            logging.info("COMPLETED deriving sections")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Derives sections')
    parser.add_argument('-id', metavar='paragraph_id', type=int, nargs='+', help='ids of the paragraphs for which sections are to be derived')

    args = parser.parse_args()
    if hasattr(args, 'id') and args.id:
        DeriveSections().derive_all(paragraph_ids=args.id)
    else:
        DeriveSections().derive_all()