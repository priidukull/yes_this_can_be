import re


class TextParser(object):
    def parse_pg_references(self, query, statutes):
        names = []
        for row in statutes:
            short_name = row["short_name"].lower()
            query = query.lower()
            if short_name in query and not (query.split(short_name)[0] and query.split(short_name)[0][-1].isalpha()):
                subqueries = query.split(short_name)[1:]
                for sub in subqueries:
                    trimmed_sub = sub.replace(" ", "")
                    if trimmed_sub and trimmed_sub[0] == "§":
                        pg_number = int(re.search("\d+", trimmed_sub).group(0))
                        names.append({"statute_id": row["id"], "pg_number": pg_number})
        return names