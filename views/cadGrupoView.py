import tkinter as tk
import sqlite3
from src.grupoCliente import GrupoCliente
from model.banco import Banco
from Utils.utils import Utils
from Utils.dataBaseUtils import DataBaseUtils

class CadGrupoView:

    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Grupo")
        self.master.geometry("365x500")
        self.buildUI()

    def buildUI(self):

        lb_codigo_grupo = tk.Label(self.master, text="Codigo do Grupo")
        lb_codigo_grupo.grid(row=0, column=0, ipadx=15, ipady=10)

        cp_codigo_grupo = tk.Entry(self.master)
        cp_codigo_grupo.grid(row=0, column=1)

        lb_nome_grupo = tk.Label(self.master, text="Nome do Grupo")
        lb_nome_grupo.grid(row=1, column=0, ipadx=15, ipady=10)

        cp_nome_grupo = tk.Entry(self.master)
        cp_nome_grupo.grid(row=1, column=1)

        option = GrupoCliente.get_grupos()

        btn_cadastrar_grupo = tk.Button(self.master, text="Cadastrar", command=lambda: self.cadastra_grupo(codigo=cp_codigo_grupo.get(),
                                                                                                           nome=cp_nome_grupo.get()))
        btn_cadastrar_grupo.grid(row=2, column=0, ipadx=80, columnspan=2)

    def cadastra_grupo(self, codigo, nome):
        try:
            msg_aviso = "Grupo cadastrado com sucesso!!"
            if codigo == '' or nome == '':
                msg_aviso = "Grupo precisa ter código e nome preenchido!"
                return

            conn = Banco.createConnection()

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.INSERT_GRUPO, {
                "p1": int(codigo),
                "p2": nome
            })
            conn.commit()
            conn.close()

        except ValueError as e:
            msg_aviso = "Código precisa ser numerico!"
        except sqlite3.Error as error:
            print(error)
            msg_aviso = "Erro ao acessar o banco de dados."
        finally:
            Utils.showMsg("Aviso!", msg_aviso)

        pass

    pass
