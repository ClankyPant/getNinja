import tkinter as tk
from tkcalendar import DateEntry
from Utils.utils import Utils
from Utils.stringUtils import StringUtils
import pandas


class CadFuncionariosContent(tk.Frame):

    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Clientes")
        self.master.geometry("500x500")
        self.buildUI()

    def buildUI(self):
        # Container 1
        frContainer_1 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        lbNome = tk.Label(frContainer_1, text="Nome Funcionario ", font=StringUtils.MAIN_FONT)
        lbNome["width"] = 15
        lbNome["anchor"] = tk.NW
        lbNome.pack(side=tk.LEFT)

        cpNomeFunc = tk.Entry(frContainer_1, font=StringUtils.MAIN_FONT)
        cpNomeFunc["width"] = 25
        cpNomeFunc.pack(side=tk.LEFT)

        # Container 2
        frContainer_2 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        lbCNPJ = tk.Label(frContainer_2, text="CNPJ/CPF ", font=StringUtils.MAIN_FONT)
        lbCNPJ["width"] = 15
        lbCNPJ["anchor"] = tk.NW
        lbCNPJ.pack(side=tk.LEFT)

        cpCNPJCPF = tk.Entry(frContainer_2, font=StringUtils.MAIN_FONT)
        cpCNPJCPF["width"] = 25
        cpCNPJCPF.pack(side=tk.LEFT)

        # Container 3
        frContainer_3 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        lbTelefone = tk.Label(frContainer_3, text="Telefone ", font=StringUtils.MAIN_FONT)
        lbTelefone["width"] = 15
        lbTelefone["anchor"] = tk.NW
        lbTelefone.pack(side=tk.LEFT)

        cpTelefone = tk.Entry(frContainer_3, font=StringUtils.MAIN_FONT)
        cpTelefone["width"] = 25
        cpTelefone.pack(side=tk.LEFT)

        # Container 4
        frContainer_4 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        lbSalario = tk.Label(frContainer_4, text="Salario ", font=StringUtils.MAIN_FONT)
        lbSalario["width"] = 15
        lbSalario["anchor"] = tk.NW
        lbSalario.pack(side=tk.LEFT)

        cpSalario = tk.Entry(frContainer_4, font=StringUtils.MAIN_FONT)
        cpSalario["width"] = 25
        cpSalario.pack(side=tk.LEFT)

        # Container 5
        frContainer_5 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        lbDateFunc = tk.Label(frContainer_5, text="Data Fundação ", font=StringUtils.MAIN_FONT)
        lbDateFunc["width"] = 15
        lbDateFunc["anchor"] = tk.NW
        lbDateFunc.pack(side=tk.LEFT)

        cpDateFunc = DateEntry(frContainer_5)
        cpDateFunc["width"] = 30
        cpDateFunc.pack(side=tk.LEFT)

        # Container 6
        frContainer_6 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        lbTipoFuncionario = tk.Label(frContainer_6, text="Tipo Funcionario ", font=StringUtils.MAIN_FONT)
        lbTipoFuncionario["width"] = 15
        lbTipoFuncionario["anchor"] = tk.NW
        lbTipoFuncionario.pack(side=tk.LEFT)

        options = [
            "Atendente",
            "Consultor",
            "RH",
            "Vendedor",
            "Técnico TI",
            "Outros"
        ]
        selectedOption = tk.StringVar()
        selectedOption.set(options[len(options)-1])
        cpTipoFunc = tk.OptionMenu(frContainer_6, selectedOption, *options)
        cpTipoFunc["width"] = 25
        cpTipoFunc.pack()

        # Container 7
        frContainer_7 = Utils.createDefaultFrame(self.master, padx=10, pady=20)

        btnCadastrar = tk.Button(frContainer_7, text="Cadastrar Funcionario",
                                 command=lambda: self.cadastrarFuncionario(nome=cpNomeFunc.get(), cnpjCpf=cpCNPJCPF.get(),
                                                                           telefone=cpTelefone.get(), salario=cpSalario.get(),
                                                                           dataFundacao=cpDateFunc.get(), tipoFuncionario=selectedOption.get()))
        btnCadastrar.pack()

        pass

    def cadastrarFuncionario(self, nome, cnpjCpf, telefone, salario, dataFundacao, tipoFuncionario):
        try:
            if salario == '':
                self.showMsg("Aviso!", "Campos de sálario precisa ser informado!")
                return


        except ValueError as e:
            self.showMsg("Aviso!", "Campo de sálario aceita apenas valores numericos.")
        pass

    @staticmethod
    def showMsg(title, value):
        tk.messagebox.showinfo(title, value)