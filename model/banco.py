import sqlite3
from Utils.dataBaseUtils import DataBaseUtils


class Banco:

    @staticmethod
    def createConnection():
        return sqlite3.connect(DataBaseUtils.ABSOLUTE_PATH)

    @staticmethod
    def createTables():
        try:
            con = Banco.createConnection()
            cursor = con.cursor()

            cursor.execute(DataBaseUtils.CREATE_CLIENTE)
            cursor.execute(DataBaseUtils.CREATE_USER)
            
            con.commit()
            con.close()

        except sqlite3.Error as error:
            print("Erro ao conectar no SQLite", error)