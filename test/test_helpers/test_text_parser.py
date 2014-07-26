from helpers.text_parser import TextParser


class TestClass(object):
    def setup(self):
        self._text_parser = TextParser()
        self._statutes = [{"short_name": "PS", "name": "Põhiseadus", "id": 11},
                          {"short_name": "AVRS", "name": "Abieluvara registri seadus", "id": 12}]

    def test_parse_pg_references_when_contains_many_references(self):
        actual = self._text_parser.parse_pg_references(query="ps§1 gsdg avrs  § 6", statutes=self._statutes)

        assert [{"statute_id": 11, "pg_number": 1}, {"statute_id": 12, "pg_number": 6}] == actual

    def test_parse_pg_references(self):
        actual = self._text_parser.parse_pg_references(query="ps § 1", statutes=self._statutes)

        assert [{"statute_id": 11, "pg_number": 1}] == actual

    def test_parse_pg_references_when_pg_is_of_length(self):
        actual = self._text_parser.parse_pg_references(query="ps § 123faf", statutes=self._statutes)

        assert [{"statute_id": 11, "pg_number": 123}] == actual

    def test_parse_pg_references_when_substring_of_short_name_matches_another_short_name(self):
        self._statutes = [{"short_name": "KRMS", "name": "Kriminaalmenetluse seadustik", "id": 11},
                          {"short_name": "MS", "name": "Metsaseadus", "id": 12}]
        actual = self._text_parser.parse_pg_references(query="krms § 255", statutes=self._statutes)

        assert [{"statute_id": 11, "pg_number": 255}] == actual

    def test_parse_pg_references_when_query_ends_with_short_name(self):
        actual = self._text_parser.parse_pg_references(query="krms", statutes=self._statutes)

        assert not actual