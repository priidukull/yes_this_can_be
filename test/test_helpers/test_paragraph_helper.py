from helpers.paragraph_helper import Helper


class TestClass():
    def test_parse_sections(self):
        row = {"id": 101, "pg_xml": "\n10\n§ 10. \nEesti raadiosagedusplaani muutmine\n\n1\n(1)\n\nTehnilise Järelevalve Amet vaatab vähemalt kord aastas Eesti raadiosagedusplaani läbi ning esitab majandus- ja kommunikatsiooniministrile ettepaneku Eesti raadiosagedusplaani muutmiseks, kui:\n\n\n1\n1) \n\nseda tingib elektroonilise side tehnoloogia areng;\n\n\n\n2\n2) \n\nmuutmise kohustus tuleneb rahvusvahelisest lepingust või\n\n\n\n3\n3) \n\nsee on vajalik riigikaitse tagamiseks.\n\n\n\nRT I\n2011-03-23\n1\n123032011001\n\n2011-05-25\n\n\n\n\n2\n(2)\n\nKäesoleva seaduse §-s 152 sätestatud konsulteerimine ei ole vajalik, kui muudatused hõlmavad §-s 21 sätestatut või ei piira Eesti raadiosagedusplaani muutmise ajal raadiosagedusi kasutavate isikute õigusi.\n\n\n\n3\n(3)\n\nKui käesoleva seaduse § 9 lõike 3 alusel antud majandus- ja kommunikatsiooniministri määrus piirab raadiosageduste kasutaja õigusi, jõustub see raadiosageduste kasutaja õigusi piiravas osas pärast kahe aasta möödumist selle avaldamise päevast, kui rahvusvahelises lepingus ei ole sätestatud teisiti.\n\n\n"}

        sections = Helper().parse_sections(row=row)

        assert sections

    def test_parse_sections_split_by_first_occurence(self):
        row = {"id": 101, "pg_header": "Omandireformi õigustatud subjektid",
               "pg_xml": "\n4\n§ 4.\nOmandireformi õigustatud subjektid\n\n\nOmandireformi õigustatud subjektid on isikud, \n\n\n"}

        sections = Helper().parse_sections(row=row)

        assert "Omandireformi õigustatud subjektid on isikud" in sections[0]["sc_xml"]

    def test_parse_sections_when_one_of_section_numbers_has_index(self):
        row = {"id": 101, "pg_header": "Header of paragraph",
               "pg_xml": "\n4\n§ 4.\nHeader of paragraph\n\n1\n(1)\n\nFirst section\n\n1\n(1<sup>1</sup>)\n\nFirst section with index\n\n\n"}

        sections = Helper().parse_sections(row=row)

        assert [{'sc_number': 1, 'paragraph_id': 101, 'sc_index_number': 0, 'sc_xml': 'First section\n'},
                {'sc_number': 1, 'paragraph_id': 101, 'sc_index_number': 1, 'sc_xml': 'First section with index\n\n\n'}] == sections