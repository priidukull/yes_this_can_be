import argparse
import logging
from app.models.section import SectionRepo
from helpers.section_helper import Helper
from app.models.point import PointRepo


class DerivePoints():
    def __init__(self):
        self._section_repo = SectionRepo()
        self._section_helper = Helper()
        self._point_mdl = PointRepo()

    def derive_all(self, section_ids=None):
        logging.info("Started deriving sections")
        sections = self._section_repo.get_all(section_ids=section_ids)
        for row in sections:
            points = self._section_helper.parse_points(row=row)
            self._point_mdl.insert_many(points)
            logging.info("COMPLETED deriving points")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Derives points')
    parser.add_argument('-id', metavar='section_id', type=int, nargs='+', help='ids of the sections for which points are to be derived')

    args = parser.parse_args()
    if hasattr(args, 'id') and args.id:
        DerivePoints().derive_all(section_ids=args.id)
    else:
        DerivePoints().derive_all()