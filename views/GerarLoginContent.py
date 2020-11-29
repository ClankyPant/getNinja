import tkinter as tk
import sqlite3
import pandas
from tkinter import messagebox
from model.banco import Banco
from Utils.StringUtils import StringUtils
from Utils.Utils import Utils
from Utils.DataBaseUtils import DataBaseUtils


class GerarLoginContent(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sistema de RH")
        self.master.geometry("250x250")
        self.buildUI()

    def buildUI(self):
        # Container 1
        frContainer_1 = Utils.createDefaultFrame(master=self.master, padX=10, padY=20)

        lbCodigo = tk.Label(frContainer_1, text="Codigo ADM", font=StringUtils.MAIN_FONT)
        lbCodigo.pack()

        # Container 2
        frContainer_2 = Utils.createDefaultFrame(master=self.master, padX=10, padY=20)

        tryCodigo = tk.Entry(frContainer_2, font=StringUtils.MAIN_FONT, show="*")
        tryCodigo.pack()

        # Container 3
        ftContainer_3 = Utils.createDefaultFrame(master=self.master, padX=10, padY=20)

        btnGerarLogin = tk.Button(ftContainer_3, text="Gerar Login", font=StringUtils.MAIN_FONT, command=lambda: self.gerarLogin(codigo=tryCodigo.get()))
        btnGerarLogin.pack()

        pass

    def gerarLogin(self, codigo):
        if pandas.notnull(codigo) and codigo == "admin":
            aviso = "Usuario Root "
            try:
                con = Banco.createConnection()
                cursor = con.cursor()

                cursor.execute(DataBaseUtils.SELECT_USER_ROOT)
                if not cursor.fetchall():
                    cursor.execute(DataBaseUtils.INSERT_USER_ROOT)
                    aviso += "criado com sucesso!"
                else:
                    aviso += "já exite!"

                tk.messagebox.showinfo("Aviso!", aviso)

                con.commit()
                con.close()
            except sqlite3.Error as error:
                print("Erro ao conectar no SQLite", error)
            finally:
                self.master.destroy()
        pass
