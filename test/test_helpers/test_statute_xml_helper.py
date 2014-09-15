from bs4 import BeautifulSoup
from helpers.statute_xml_helper import Helper


class TestClass():
    def test_parse_paragraphs(self):
        row = {"statute_id": 1, "xml": """
                <paragrahv id="para42b2">
                    <kuvatavNr><![CDATA[§ 42<sup>2</sup>.]]></kuvatavNr>
                    <paragrahvPealkiri>Registrikaardi ümberkirjutamine ametiülesande korras</paragrahvPealkiri>
                </paragrahv>"""}

        paragraphs = Helper().parse_paragraphs(row=row)

        assert paragraphs[0]["pg_index_number"] == 2

