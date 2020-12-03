import sqlite3
import tkinter as tk
from views.gerarLoginADMView import GerarLoginContent
from views.cadClienteView import CadFuncionariosContent
from views.cadGrupoView import CadGrupoView
from Utils.stringUtils import StringUtils
from Utils.utils import Utils
from Utils.dataBaseUtils import DataBaseUtils
from model.banco import Banco


class Main(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Var Login
        self.frContainer_1 = None
        self.lbTitle = None
        self.frContainer_2 = None
        self.lbLogin = None
        self.loginField = None
        self.trContainer_3 = None
        self.lbSenha = None
        self.senhaField = None
        self.frContainer_4 = None
        self.btnLogin = None
        self.frContainer_5 = None
        self.btnGerarLogin = None
        self.pack()
        self.buildUI()

    def buildUI(self):
        # Container 1
        self.frContainer_1 = Utils.createDefaultFrame(master=self.master, padx=20, pady=20)

        self.lbTitle = tk.Label(self.frContainer_1, text="GetNinja", font=StringUtils.MAIN_FONT)
        self.lbTitle.pack()

        # Container 2
        self.frContainer_2 = Utils.createDefaultFrame(master=self.master, padx=10, pady=20)

        self.lbLogin = tk.Label(self.frContainer_2, text="Login", font=StringUtils.MAIN_FONT)
        self.lbLogin["width"] = 5
        self.lbLogin["anchor"] = tk.NW
        self.lbLogin.pack(side=tk.LEFT)

        self.loginField = tk.Entry(self.frContainer_2)
        self.loginField["width"] = 25
        self.loginField.pack(side=tk.LEFT)

        # Container 3
        self.trContainer_3 = Utils.createDefaultFrame(master=self.master, padx=20, pady=5)

        self.lbSenha = tk.Label(self.trContainer_3, text="Senha", font=StringUtils.MAIN_FONT)
        self.lbSenha["width"] = 5
        self.lbSenha["anchor"] = tk.NW
        self.lbSenha.pack(side=tk.LEFT)

        self.senhaField = tk.Entry(self.trContainer_3, show="*")
        self.senhaField["width"] = 25
        self.senhaField.pack(side=tk.LEFT)

        # Container 4
        self.frContainer_4 = Utils.createDefaultFrame(master=self.master, padx=20, pady=5)

        self.btnLogin = tk.Button(self.frContainer_4, text="Login", font=StringUtils.MAIN_FONT, width=23,
                                  command=self.logar)
        self.btnLogin.pack()

        # Container 5
        self.frContainer_5 = Utils.createDefaultFrame(master=self.master, padx=20, pady=5)

        self.btnGerarLogin = tk.Button(self.frContainer_5, text="Gerar Login ADM", width=23, font=StringUtils.MAIN_FONT,
                                       command=self.openGerarLoginContent)
        self.btnGerarLogin.pack()

        pass

    def openCadFuncionario(self):
        frameCadFuncionario = tk.Toplevel(self.master)
        CadFuncionariosContent(frameCadFuncionario)

        pass

    def openGerarLoginContent(self):
        view = tk.Toplevel(self.master)
        GerarLoginContent(view)
        pass

    def buildMainScreenMenus(self):
        mainMenuBar = tk.Menu(self.master)
        self.master.config(menu=mainMenuBar)

        registerMenu = tk.Menu(mainMenuBar)
        mainMenuBar.add_cascade(label="Cadastros", menu=registerMenu)
        registerMenu.add_command(label="Cadastro de Cliente", command=self.openCadFuncionario)
        registerMenu.add_command(label="Cadastro de Grupos", command=self.open_cad_grupos)

        optionMenu = tk.Menu(mainMenuBar)
        mainMenuBar.add_cascade(label="Opções", menu=optionMenu)
        optionMenu.add_command(label="Exit", command=self.master.quit)

        pass

    def open_cad_grupos(self):
        view = tk.Toplevel(self.master)
        CadGrupoView(view)

        pass

    def logar(self):
        try:
            conn = Banco.createConnection()
            cursor = conn.cursor()
            cursor.execute(DataBaseUtils.SELECT_USER_BY_LOGIN.replace(":p1", '\'' + self.loginField.get() + '\'').replace(":p2",
                                                                                                         '\'' + self.senhaField.get() + '\''))
            if cursor.fetchone():
                self.destroyLoginFields()
                self.buildMainScreenMenus()
            else:
                tk.messagebox.showinfo("Aviso!", "Usuario não encontrado, ou credencial incorreta!")

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Erro..:", e)

        pass

    def destroyLoginFields(self):
        self.frContainer_1.destroy()
        self.lbTitle.destroy()
        self.frContainer_2.destroy()
        self.lbLogin.destroy()
        self.loginField.destroy()
        self.trContainer_3.destroy()
        self.lbSenha.destroy()
        self.senhaField.destroy()
        self.frContainer_4.destroy()
        self.btnLogin.destroy()
        self.frContainer_5.destroy()
        self.btnGerarLogin.destroy()


if __name__ == '__main__':
    t = Banco.createTables()
    root = tk.Tk()
    root.title("Sistema de CRUD")
    root.geometry("850x450")

    Main(master=root)

    root.mainloop()