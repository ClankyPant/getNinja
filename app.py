import sqlite3
import tkinter as tk
from views.GerarLoginContent import GerarLoginContent
from Utils.StringUtils import StringUtils
from Utils.Utils import Utils
from Utils.DataBaseUtils import DataBaseUtils
from model.banco import Banco


class Main(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buildUI()

    def buildUI(self):
        # Container 1
        frContainer_1 = Utils.createDefaultFrame(master=self.master, padX=20, padY=20)

        lbTitle = tk.Label(frContainer_1, text="GetNinja", font=StringUtils.MAIN_FONT)
        lbTitle.pack()

        # Container 2
        frContainer_2 = Utils.createDefaultFrame(master=self.master, padX=10, padY=20)

        lbLogin = tk.Label(frContainer_2, text="Login", font=StringUtils.MAIN_FONT)
        lbLogin["width"] = 5
        lbLogin["anchor"] = tk.NW
        lbLogin.pack(side=tk.LEFT)

        loginField = tk.Entry(frContainer_2)
        loginField["width"] = 25
        loginField.pack(side=tk.LEFT)

        # Container 3
        trContainer_3 = Utils.createDefaultFrame(master=self.master, padX=20, padY=5)

        lbSenha = tk.Label(trContainer_3, text="Senha", font=StringUtils.MAIN_FONT)
        lbSenha["width"] = 5
        lbSenha["anchor"] = tk.NW
        lbSenha.pack(side=tk.LEFT)

        senhaField = tk.Entry(trContainer_3, show="*")
        senhaField["width"] = 25
        senhaField.pack(side=tk.LEFT)

        # Container 4
        frContainer_4 = Utils.createDefaultFrame(master=self.master, padX=20, padY=5)

        btnLogin = tk.Button(frContainer_4, text="Login", font=StringUtils.MAIN_FONT, width=23, command=lambda: self.logar(user=loginField.get(), password=senhaField.get()))
        btnLogin.pack()

        # Container 5
        frContainer_5 = Utils.createDefaultFrame(master=self.master, padX=20, padY=5)

        btnGerarLogin = tk.Button(frContainer_5, text="Gerar Login ADM", width=23, font=StringUtils.MAIN_FONT,
                                  command=self.gerarLoginOpenView)
        btnGerarLogin.pack()

    def logar(self, user, password):
        try:
            conn = Banco.createConnection()
            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.SELECT_USER_BY_LOGIN.replace(":p1", '\''+user+'\'').replace(":p2", '\''+password+'\''))

            if cursor.fetchone():
                print("Logado com Sucesso!!")

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Erro..:", e)

        pass

    def gerarLoginOpenView(self):
        view = tk.Toplevel(self.master)
        GerarLoginContent(view)
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Sistema de RH")
    root.geometry("850x450")

    Main(master=root)

    root.mainloop()
