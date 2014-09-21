from helpers.section_helper import Helper


class TestClass():
    def test_parse_points(self):
        row = {"id": 101, "sc_xml": "Finantsinspektsioon võib krediidiasutusele kehtestada moratooriumi, kui\n\n\n1\n1) \n\nkrediidiasutus tulenevalt oma finantsseisundist ei täida tähtaegselt kas või ühte oma kohustust hoiustajate ees või"}

        points = Helper().parse_points(row)

        assert 2 == points.__len__()

    def test_parse_pt_numbers_raw(self):
        sc_xml = "\n\n\n10\n10<sup>1</sup>) \n\n"

        pt_numbers_raw = Helper()._parse_pt_numbers_raw(sc_xml=sc_xml)

        assert pt_numbers_raw