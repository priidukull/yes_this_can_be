import logging

from external import statute_crawler
from app.models import statute, statute_xml


class FillStatuteXml(object):
    def __init__(self):
        self._statute_crawler = statute_crawler.StatuteCrawler()
        self._statute_xml_mdl = statute_xml.StatuteXml()

    def collect_statute_xml(self):
        statutes = statute.Statute().get_all()
        for row in statutes:
            url = self._statute_crawler.fetch_xml_url(short_name=row["short_name"])
            xml = self._statute_crawler.fetch_xml_from_file(url=url)
            self._statute_xml_mdl.insert(url=url, xml=xml, statute_id=row["id"])
            logging.info("INSERTED url=%s, statute_id=%s")


if __name__ == "__main__":
    FillStatuteXml().collect_statute_xml()
