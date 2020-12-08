import tkinter as tk
from tkinter import ttk
import sqlite3
from utils.utils import Utils
from utils.dataBaseUtils import DataBaseUtils
from model.banco import Banco


class CadFuncionariosContent:

    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Clientes")
        self.master.geometry("750x750")
        self.flagOnConsulta = False

        # LABELS
        self.lb_id_cliente = tk.Label(self.master, text="Cliente ID")
        self.lb_nome_cliente = tk.Label(self.master, text="Nome Cliente")
        self.lb_cnpj_cliente = tk.Label(self.master, text="CNPJ/CPF")
        self.lb_telefone_cliente = tk.Label(self.master, text="Telefone")
        self.lb_grupo_cliente = tk.Label(self.master, text="Código Grupo")

        # CAMPOS
        self.cp_id_cliente = tk.Entry(self.master, width=10)
        self.cp_nome_cliente = tk.Entry(self.master)
        self.cp_cnpj_cliente = tk.Entry(self.master)
        self.cp_telefone_cliente = tk.Entry(self.master)
        self.cp_grupo_cliente = tk.Entry(self.master)

        # BUTTONS
        self.btn_buscar = tk.Button(self.master, text="Buscar", command=self.buscar_cliente)
        self.btn_cadastrar = tk.Button(self.master, text="Cadastrar", command=self.cadastra_cliente)
        self.btn_excluir = tk.Button(self.master, text="Excluir", command=self.excluir_cliente)
        self.btn_limpar = tk.Button(self.master, text="Limpar", command=self.limpar_campos)
        self.btn_limpar.config(state="disable")
        self.btn_atualizar = tk.Button(self.master, text="Atualizar", command=self.atualizar_cliente)
        self.btn_atualizar.config(state="disable")

        # TREE's
        self.tree_main = ttk.Treeview(self.master, columns=('id', 'Nome Cliente', 'Telefone'), show='headings')
        self.buildTree()

        self.buildUI()

    def buildUI(self):
        self.lb_id_cliente .grid(row=0, column=0, ipadx=75, ipady=10)
        self.cp_id_cliente.grid(row=0, column=1, padx=15, sticky=tk.E)
        self.btn_buscar.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.btn_limpar.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.lb_nome_cliente.grid(row=1, column=0, ipadx=75, ipady=10)
        self.cp_nome_cliente.grid(row=1, column=1)

        self.lb_cnpj_cliente.grid(row=2, column=0, ipadx=75, ipady=10)
        self.cp_cnpj_cliente.grid(row=2, column=1)

        self.lb_telefone_cliente.grid(row=3, column=0, ipadx=75, ipady=10)
        self.cp_telefone_cliente.grid(row=3, column=1)

        self.lb_grupo_cliente.grid(row=4, column=0, ipadx=75, ipady=10)
        self.cp_grupo_cliente.grid(row=4, column=1)

        self.btn_cadastrar.grid(row=5, ipadx=25, column=0, columnspan=3)
        self.btn_excluir.grid(row=5, ipadx=25, column=1, columnspan=2)
        self.btn_atualizar.grid(row=5, ipadx=25, column=2, columnspan=2)

        self.tree_main.grid(row=6, column=0, padx=50, pady=50, columnspan=10)

        pass

    def cadastra_cliente(self):
        msg_aviso = "Cliente cadastrado com sucesso!!"

        nome = self.cp_nome_cliente.get()
        cnpj = self.cp_cnpj_cliente.get()
        telefone = self.cp_telefone_cliente.get()
        cod_grupo = self.cp_grupo_cliente.get()

        try:
            conn = Banco.createConnection()

            if self.flagOnConsulta:
                msg_aviso = "Você precisa limpar os campos antes de cadastrar um novo cliente!"
                return
            elif cnpj == '' or nome == '':
                msg_aviso = "Ao menos o nome e CNPJ precisam estar preenchidos para cadastro!"
                return

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.INSERT_CLIENTE, {
                "p1": nome,
                "p2": cnpj,
                "p3": telefone,
                "p4": cod_grupo
            })
            conn.commit()

        except ValueError as e:
            msg_aviso = "Campo de sálario e Qtd de dependentes aceita apenas valores numericos."
        except sqlite3.Error as error:
            print(error)
            msg_aviso = "Erro ao acessar o banco de dados."
        finally:
            conn.close()
            Utils.showMsg("Aviso!", msg_aviso)
            self.refresh_tree()

        pass

    def excluir_cliente(self):
        msg_aviso = "Cliente deletado com sucesso!!"
        id_cliente = self.cp_id_cliente.get()
        try:
            conn = Banco.createConnection()

            if id_cliente == '':
                msg_aviso = "ID precisa estar preenchido"
                return
            elif not self.flagOnConsulta:
                msg_aviso = "Você precisa primeiro consultar um cliente"
                return

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.DELETE_CLIENTE, {
                "p1": id_cliente
            })
            conn.commit()

        except sqlite3.Error as error:
            print(error)
            msg_aviso = "Erro ao acessar o banco de dados."
        finally:
            conn.close()
            self.limpar_campos()
            self.refresh_tree()
            Utils.showMsg("Aviso!", msg_aviso)

        pass

    def buscar_cliente(self):
        id_cliente = self.cp_id_cliente.get()
        is_busca_sucesso = True
        self.limpar_campos()
        try:
            conn = Banco.createConnection()

            if id_cliente == '':
                Utils.showMsg("Aviso!", "ID precisa estar preenchido")
                is_busca_sucesso = False
                return

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.SELECT_CLIENTE_BY_ID, {
                "p1": id_cliente
            })

            rows = cursor.fetchone()
            if rows:
                self.cp_id_cliente.insert(0, id_cliente)
                self.cp_nome_cliente.insert(0, rows[0])
                self.cp_telefone_cliente.insert(0, rows[1])
                self.cp_cnpj_cliente.insert(0, rows[2])
                self.cp_grupo_cliente.insert(0, rows[3])
            else:
                Utils.showMsg("Aviso!", "Cliente não encontrado!")
                is_busca_sucesso = False

        except sqlite3.Error as error:
            print(error)
        finally:
            conn.close()
            if is_busca_sucesso:
                self.flagOnConsulta = True
                self.cp_id_cliente.config(state="readonly")
                self.btn_limpar.config(state="active")
                self.btn_atualizar.config(state="active")
        pass

    def atualizar_cliente(self):
        try:
            if not self.flagOnConsulta:
                Utils.showMsg("Aviso!", "Primeiro é necessário consultar um cliente para depois alterar o seu cadastro!")
                return

            conn = Banco.createConnection()

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.UPDATE_CLIENTE_BY_ID, {
                "p1": self.cp_nome_cliente.get(),
                "p2": self.cp_telefone_cliente.get(),
                "p3": self.cp_cnpj_cliente.get(),
                "p4": self.cp_grupo_cliente.get(),
                "p5": self.cp_id_cliente.get(),
            })
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            Utils.showMsg("Aviso!", "Cliente atualizado com sucesso!")
            self.refresh_tree()
        pass

    def limpar_campos(self):
        self.cp_nome_cliente.delete(0, 'end')
        self.cp_cnpj_cliente.delete(0, 'end')
        self.cp_telefone_cliente.delete(0, 'end')
        self.cp_grupo_cliente.delete(0, 'end')
        self.flagOnConsulta = False
        self.btn_limpar.config(state="disable")
        self.btn_atualizar.config(state="disable")
        self.cp_id_cliente.config(state="normal")
        self.cp_id_cliente.delete(0, 'end')
        pass

    def buildTree(self):
        self.tree_main['columns'] = ("id", "Nome", "CNPJ", "Telefone", "CodGrupo")
        # self.tree_main.column("#0", width=125, anchor=tk.N)
        self.tree_main.column("id", width=125, anchor=tk.N)
        self.tree_main.column("Nome", width=125, anchor=tk.N)
        self.tree_main.column("CNPJ", width=125, anchor=tk.N)
        self.tree_main.column("Telefone", width=125, anchor=tk.N)
        self.tree_main.column("CodGrupo", width=125, anchor=tk.N)

        # self.tree_main.heading("#0", text='label', anchor=tk.W)
        self.tree_main.heading("id", text="ID")
        self.tree_main.heading("Nome", text="Nome Cliente")
        self.tree_main.heading("CNPJ", text=" CNPJ/CPF")
        self.tree_main.heading("Telefone", text="Telefone")
        self.tree_main.heading("CodGrupo", text="Cód. Grupo")

        self.refresh_tree()
        pass

    def refresh_tree(self):
        try:
            conn = Banco.createConnection()

            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.SELECT_ALL_CLIENTES)

            rows = cursor.fetchall()

            # Limpando registros que já existem
            for i in self.tree_main.get_children():
                self.tree_main.delete(i)

            # Adicionando todos os clientes existentes

            for row in rows:
                self.tree_main.insert(parent='', index='end', iid=row[0], text='', values=(row[0], row[1], row[2], row[3], row[4]))
                pass

            conn.close()

        except sqlite3.Error as error:
            print(error)
        pass
