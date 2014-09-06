import re


class Helper():
    def parse_sections(self, row):
        paragraph = row["id"]
        pg_xml = row["pg_xml"]
        sc_numbers_raw = re.findall("\\n\d\\n\(\d\)\\n\\n", pg_xml)
        sections = []
        for idx, sc_number_raw in enumerate(sc_numbers_raw):
            section_text = pg_xml.split(sc_number_raw)[1]
            try:
                section_text = section_text.split(sc_numbers_raw[idx+1])[0]
            except IndexError:
                pass
            section_text = section_text.split("\n\n\n\nRT")[0]
            sc_number = int(re.search("\((.*)\)", sc_number_raw).group(1))
            sections.append({"paragraph": paragraph, "sc_number": sc_number, "text": section_text})
        return sections

