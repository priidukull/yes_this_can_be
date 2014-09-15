from bs4 import BeautifulSoup


class Helper(object):
    def parse_paragraphs(self, row):
        statute_id = row["statute_id"]
        xml = row["xml"]
        soup = BeautifulSoup(xml)
        all_pg_values = []
        for paragraph in soup.find_all("paragrahv"):
            if "§" in paragraph.text:
                pg_values = {"statute_id": statute_id, "pg_xml": paragraph.text}
                try:
                    pg_values.update({"pg_header": paragraph.find("paragrahvpealkiri").text})
                except AttributeError:
                    pg_values.update({"pg_header": None})
                pg_number_raw = paragraph.find("kuvatavnr").text.strip()
                if pg_number_raw:
                    pg_number_rawish = pg_number_raw[2:-1]
                    try:
                        pg_values.update({"pg_number": int(pg_number_rawish), "pg_index_number": 0})
                        all_pg_values.append(pg_values)
                    except ValueError:
                        try:
                            pg_values.update({"pg_number": int(pg_number_rawish.split("<")[0])})
                            pg_number_soup = BeautifulSoup(pg_number_rawish)
                            pg_index_number = pg_number_soup.find("sup").text
                            pg_index_number = int(pg_index_number)
                            pg_values.update({"pg_index_number": pg_index_number})
                            all_pg_values.append(pg_values)
                        except ValueError:
                            pass
        return all_pg_values