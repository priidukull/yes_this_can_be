from os import path

from singletons import DbConnection

class DB(object):
    def __init__(self):
        self.intransaction = []
        self.rollback()
    def begin(self, name):
        self.intransaction.append(name)
    def rollback(self):
        DbConnection().engine.execute(open(path.relpath("test/delete_from_all_tables.sql"), "r", encoding="utf-8").read())