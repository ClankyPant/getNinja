import sqlite3
from Utils.DataBaseUtils import DataBaseUtils


class Banco:

    def __init__(self):
        self.createTables()

    def createTables(self):
        try:
            con = self.createConnection()
            con.cursor()

            # c.execute(DataBaseUtils.CREATE_FUNCIONARIO)
            con.execute(DataBaseUtils.CREATE_USER)

            con.commit()
            con.close()

        except sqlite3.Error as error:
            print("Erro ao conectar no SQLite", error)

    @staticmethod
    def createConnection():
        return sqlite3.connect(DataBaseUtils.ABSOLUTE_PATH)