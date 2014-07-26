from os import path

from app.models.model import Model


class DB(object):
    def __init__(self):
        self.intransaction = []
        self.rollback()
    def begin(self, name):
        self.intransaction.append(name)
    def rollback(self):
        Model()._conn.execute(open(path.relpath("test/delete_from_all_tables.sql"), "r", encoding="utf-8").read())