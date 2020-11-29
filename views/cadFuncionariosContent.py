import tkinter as tk
from Utils.utils import Utils
from Utils.stringUtils import StringUtils


class CadFuncionariosContent():
    def __init__(self, master=None):
        self.master = master
        self.buildUI()

    def buildUI(self):
        # Container 1
        frContainer_1 = Utils.createDefaultFrame(self.master, padX=10, padY=20)
        lb = tk.Label(frContainer_1, text="Nome Funcionario: ", font=StringUtils.MAIN_FONT)
        lb.grid(row=0, column=0)

        lbNomeFuncionario = tk.Entry(frContainer_1, font=StringUtils.MAIN_FONT)
        lbNomeFuncionario.grid(row=0, column=1)

        # Container 2
        frContainer_2 = Utils.createDefaultFrame(self.master, padX=10, padY=20)

        pass
