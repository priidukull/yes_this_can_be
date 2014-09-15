import re


class Helper():
    def parse_sections(self, row):
        paragraph_id = row["id"]
        pg_xml = row["pg_xml"]
        sc_numbers_raw = re.findall("\\n\d\\n\(\d\)\\n\\n", pg_xml)
        sections = []
        for idx, sc_number_raw in enumerate(sc_numbers_raw):
            sc_xml = pg_xml.split(sc_number_raw)[1]
            try:
                sc_xml = sc_xml.split(sc_numbers_raw[idx+1])[0]
            except IndexError:
                sc_xml = sc_xml.split("\n\n\n<")[0]
            sc_xml = sc_xml.split("\n\n\nRT")[0]
            sc_number = int(re.search("\((.*)\)", sc_number_raw).group(1))
            sections.append({"paragraph_id": paragraph_id, "sc_number": sc_number, "sc_xml": sc_xml})
        if not sections:
            sc_xml = pg_xml.split(row["pg_header"], 1)[1]
            sections.append({"paragraph_id": paragraph_id, "sc_number": 0, "sc_xml": sc_xml})
        return sections

