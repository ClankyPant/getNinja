import tkinter as tk
import sqlite3
from tkcalendar import DateEntry
from Utils.utils import Utils
from Utils.stringUtils import StringUtils
from Utils.dataBaseUtils import DataBaseUtils
from model.banco import Banco
import pandas


class CadFuncionariosContent:

    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Clientes")
        self.master.geometry("750x500")
        self.buildUI()

    def buildUI(self):
        lb_id_cliente = tk.Label(self.master, text="Cliente ID")
        lb_id_cliente .grid(row=0, column=0, ipadx=75, ipady=10)

        cp_id_cliente = tk.Entry(self.master, width=10)
        cp_id_cliente.grid(row=0, column=1)

        lb_nome_cliente = tk.Label(self.master, text="Nome Cliente")
        lb_nome_cliente.grid(row=1, column=0, ipadx=75, ipady=10)

        cp_nome_cliente = tk.Entry(self.master)
        cp_nome_cliente.grid(row=1, column=1)

        lb_cnpj_cliente = tk.Label(self.master, text="CNPJ")
        lb_cnpj_cliente.grid(row=2, column=0, ipadx=75, ipady=10)

        cp_cnpj_cliente = tk.Entry(self.master)
        cp_cnpj_cliente.grid(row=2, column=1)

        lb_telefone_cliente = tk.Label(self.master, text="Telefone")
        lb_telefone_cliente.grid(row=3, column=0, ipadx=75, ipady=10)

        cp_telefone_cliente = tk.Entry(self.master)
        cp_telefone_cliente.grid(row=3, column=1)

        lb_grupo_cliente = tk.Label(self.master, text="Código Grupo")
        lb_grupo_cliente.grid(row=4, column=0, ipadx=75, ipady=10)

        cp_grupo_cliente = tk.Entry(self.master)
        cp_grupo_cliente.grid(row=4, column=1)

        btn_cadastrar = tk.Button(self.master, text="Cadastrar", command=lambda: self.cadastra_cliente(nome=cp_nome_cliente.get(),
                                                                                                       cnpj=cp_cnpj_cliente.get(),
                                                                                                       telefone=cp_telefone_cliente.get(),
                                                                                                       cod_grupo=cp_grupo_cliente.get()))
        btn_cadastrar.grid(row=5, column=0, ipadx=75, pady=20)

        btn_excluir = tk.Button(self.master, text="Excluir", command=lambda: self.excluir_cliente(cp_id_cliente.get()))
        btn_excluir.grid(row=5, column=1)

        pass

    def cadastra_cliente(self, nome, cnpj, telefone, cod_grupo):
        msg_aviso = "Cliente cadastrado com sucesso!!"
        try:
            conn = Banco.createConnection()

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.INSERT_CLIENTE, {
                "p1": nome,
                "p2": cnpj,
                "p3": telefone,
                "p4": cod_grupo
            })
            conn.commit()
            conn.close()

        except ValueError as e:
            msg_aviso = "Campo de sálario e Qtd de dependentes aceita apenas valores numericos."
        except sqlite3.Error as error:
            print(error)
            msg_aviso = "Erro ao acessar o banco de dados."
        finally:
            Utils.showMsg("Aviso!", msg_aviso)

        pass

    def excluir_cliente(self, id_cliente):
        msg_aviso = "Cliente deletado com sucesso!!"
        try:
            if (id_cliente == ''):
                msg_aviso = "ID precisa estar preenchido"
                return

            conn = Banco.createConnection()

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.DELETE_CLIENTE, {
                "p1": id_cliente
            })
            conn.commit()
            conn.close()

        except sqlite3.Error as error:
            print(error)
            msg_aviso = "Erro ao acessar o banco de dados."
        finally:
            Utils.showMsg("Aviso!", msg_aviso)

        pass
