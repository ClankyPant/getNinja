import tkinter as tk
import sqlite3
import pandas
from tkinter import messagebox
from model.banco import Banco
from Utils.stringUtils import StringUtils
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

        btn_cadastrar_grupo = tk.Button(self.master, text="Cadastrar")
        btn_cadastrar_grupo.grid(row=2, column=0, ipadx=80, columnspan=2)

    pass
