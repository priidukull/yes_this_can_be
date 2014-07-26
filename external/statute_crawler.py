from os import path
import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

import requests


class StatuteCrawler(object):
    def __init__(self):
        self._RIIGITEATAJA_URL = "https://www.riigiteataja.ee"

    def fetch_statutes(self):
        xml = requests.get("https://www.riigiteataja.ee/lyhendid.html").text
        xml = xml.replace("&nbsp;", " ")
        root = ET.fromstring(xml)
        statutes = [{"name": statute[0][0].text, "short_name": statute[1][0].text} for statute in root[1][0][3][2][0][1]]
        return statutes

    def fetch_as_text(self, url):
        return requests.get(url).text

    def fetch_xml_url(self, short_name):
        page = self.fetch_as_text(url="%s/akt/%s" %(self._RIIGITEATAJA_URL, short_name))
        soup = BeautifulSoup(page)
        for link in soup.find_all("a"):
            if link.get_text() == "XML failina":
                return "%s%s" % (self._RIIGITEATAJA_URL, link.get("href"))

    def fetch_xml_from_file(self, url):
        urllib.request.urlretrieve(url, "file.xml")
        xml = open(path.relpath("file.xml"), "r").read()
        return xml