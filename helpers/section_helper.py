import re


class Helper():
    def parse_points(self, row):
        section_id = row["id"]
        sc_xml = row["sc_xml"]
        pt_numbers_raw = self._parse_pt_numbers_raw(sc_xml)
        points = []
        if pt_numbers_raw:
            point_zero_text = sc_xml.split(pt_numbers_raw[0])[0]
            if point_zero_text:
                points.append({"section_id": section_id, "pt_number": 0, "pt_text": point_zero_text, "pt_index_number": 0})
        for idx, pt_number_raw in enumerate(pt_numbers_raw):
            pt_text = sc_xml.split(pt_number_raw)[1]
            try:
                pt_text = pt_text.split(pt_numbers_raw[idx+1])[0]
            except IndexError:
                pt_text = pt_text.split("\n\n\n<")[0]
            pt_text = pt_text.split("\n\n\nRT")[0]
            try:
                pt_number = int(re.search("(\d+)\)", pt_number_raw).group(1))
                points.append({"section_id": section_id, "pt_number": pt_number, "pt_text": pt_text, "pt_index_number": 0})
            except AttributeError:
                pt_number = int(re.search("(\d+)<sup>\d+</sup>\)", pt_number_raw).group(1))
                pt_index_number = int(re.search("\d+<sup>(\d+)</sup>\)", pt_number_raw).group(1))
                points.append({"section_id": section_id, "pt_number": pt_number, "pt_text": pt_text, "pt_index_number": pt_index_number})
        if not points:
            points.append({"section_id": section_id, "pt_number": 0, "pt_text": sc_xml, "pt_index_number": 0})
        return points

    def _parse_pt_numbers_raw(self, sc_xml):
        return re.findall("\\n\\n\\n\d+\\n\d+<.+>\)|\\n\\n\\n\d+\\n\d+\)", sc_xml)