from app.models.paragraph import Paragraph
from app.models.section import Section
from helpers.paragraph_helper import Helper


class DeriveSections():
    def __init__(self):
        self._paragraph_helper = Helper()
        self._paragraph_mdl = Paragraph()
        self._section_mdl = Section()

    def derive_all(self):
        paragraphs = self._paragraph_mdl.get_all()
        for row in paragraphs:
            sections = self._paragraph_helper.parse_sections(row=row)
            self._section_mdl.insert_many(sections=sections)



if __name__ == "__main__":
    DeriveSections().derive_all()