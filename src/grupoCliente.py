from model.banco import Banco
from Utils.dataBaseUtils import DataBaseUtils
from Utils.utils import Utils
import sqlite3


class GrupoCliente:
    __codigo = None
    __nome = None

    def __init__(self, codigo, nome):
        self.set_codigo(codigo)
        self.set_nome(nome)
        pass

    def set_codigo(self, codigo):
        self.codigo = codigo
        pass

    def set_nome(self, nome):
        self.nome = nome
        pass

    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome

    def get_grupos(self):
        try:
            conn = Banco.createConnection()

            cursor = conn.cursor()
            list_grupo = cursor.execute(DataBaseUtils.SELECT_GRUPOS).fetchall()

            conn.close()
            return list_grupo
        except ValueError as e:
            msg_aviso = "Código precisa ser numerico!"
        except sqlite3.Error as error:
            print(error)
            msg_aviso = "Erro ao acessar o banco de dados."
        finally:
            Utils.showMsg("Aviso!", msg_aviso)
        pass

    pass
