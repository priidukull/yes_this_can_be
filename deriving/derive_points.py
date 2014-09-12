from app.models.section import SectionRepo
from helpers.section_helper import Helper
from app.models.point import PointRepo


class DerivePoints():
    def __init__(self):
        self._section_repo = SectionRepo()
        self._section_helper = Helper()
        self._point_mdl = PointRepo()

    def derive_all(self):
        sections = self._section_repo.get_all()
        for row in sections:
            points = self._section_helper.parse_points(row=row)
            self._point_mdl.insert_many(points)


if __name__ == "__main__":
    DerivePoints().derive_all()