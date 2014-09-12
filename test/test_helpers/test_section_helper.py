from helpers.section_helper import Helper


class TestClass():
    def test_parse_points(self):
        row = {"id": 101, "sc_xml": "Finantsinspektsioon võib krediidiasutusele kehtestada moratooriumi, kui\n\n\n1\n1) \n\nkrediidiasutus tulenevalt oma finantsseisundist ei täida tähtaegselt kas või ühte oma kohustust hoiustajate ees või"}

        points = Helper().parse_points(row)

        assert 2 == points.__len__()