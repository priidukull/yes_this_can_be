import re


class Helper():
  def parse_sections(self, row):
    paragraph_id = row["id"]
    pg_xml = row["pg_xml"]
    sc_numbers_raw = self._parse_sc_numbers_raw(pg_xml)
    sections = []
    for idx, sc_number_raw in enumerate(sc_numbers_raw):
      sc_xml = pg_xml.split(sc_number_raw)[1]
      try:
        sc_xml = sc_xml.split(sc_numbers_raw[idx + 1])[0]
      except IndexError:
        sc_xml = sc_xml.split("\n\n\n<")[0]
      sc_xml = sc_xml.split("\n\n\nRT")[0]
      try:
        sc_number = int(re.search("\((\d+)\)", sc_number_raw).group(1))
        if self._not_poers_pg_9_sc_9(sc_xml):
          sections.append({"paragraph_id": paragraph_id, "sc_number": sc_number, "sc_xml": sc_xml, "sc_index_number": 0})
      except AttributeError:
        sc_number = int(re.search("\((\d+)<sup>\d+</sup>\)", sc_number_raw).group(1))
        sc_index_number = int(re.search("\(\d+<sup>(\d+)</sup>\)", sc_number_raw).group(1))
        sections.append({"paragraph_id": paragraph_id,
                         "sc_number": sc_number,
                         "sc_xml": sc_xml,
                         "sc_index_number": sc_index_number})
    if not sections:
      sc_xml = pg_xml.split(row["pg_header"], 1)[1]
      sections.append({"paragraph_id": paragraph_id, "sc_number": 0, "sc_xml": sc_xml})
    return sections

  def _parse_sc_numbers_raw(self, pg_xml):
    return re.findall("\\n\d+\\n\(\d+<.+>\)\\n\\n|\\n\d+\\n\(\d+\)\\n\\n", pg_xml)

  def _not_poers_pg_9_sc_9(self, sc_xml):
    return "[Lõike 9 sõnastus alates 01.01.2004]" not in sc_xml