from external import statute_crawler


class TestClass(object):
    def setup(self):
        self._statute_crawler = statute_crawler.StatuteCrawler()

    def test_fetch_xml_from_file(self):
        actual = self._statute_crawler.fetch_xml_from_file(url="https://www.riigiteataja.ee/akt/123122013036.xml")

        assert "Abieluvararegistri" in actual

    def test_fetch_xml_from_file_assert_contains_estonian_char(self):
        actual = self._statute_crawler.fetch_xml_from_file(url="https://www.riigiteataja.ee/akt/123122013036.xml")

        assert "õ" in actual

    def test_fetch_xml_url(self):
        expected = "https://www.riigiteataja.ee/akt/123122013036.xml"

        actual = self._statute_crawler.fetch_xml_url(short_name="AVRS")

        assert expected == actual
