import tkinter as tk
import sqlite3
from tkcalendar import DateEntry
from Utils.utils import Utils
from Utils.stringUtils import StringUtils
from Utils.dataBaseUtils import DataBaseUtils
from model.banco import Banco


class CadFuncionariosContent:

    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Clientes")
        self.master.geometry("750x500")
        self.buildUI()

    def buildUI(self):
        lb_nome_cliente = tk.Label(self.master, text="Nome Cliente")
        lb_nome_cliente.grid(row=0, column=0, ipadx=75, ipady=10)

        cp_nome_cliente = tk.Entry(self.master)
        cp_nome_cliente.grid(row=0, column=1)

        lb_sexo = tk.Label(self.master, text="Sexo")
        lb_sexo.grid(row=1, column=0, ipadx=75, ipady=10)

        sex_options = [
            "M",
            "F"
        ]
        selected_option_sexo = tk.StringVar()
        selected_option_sexo.set(sex_options[0])
        cp_sexo = tk.OptionMenu(self.master, selected_option_sexo, *sex_options)
        cp_sexo['width'] = 15
        cp_sexo.grid(row=1, column=1)

        pass

    # def cadastrarFuncionario(self, nome, sexo, qtdDependentes, salario, dataAdmissao, setorFunc):
    #     msgAviso = None
    #     try:
    #         # Alterações e validações
    #
    #         setorFunc = setorFunc[0:3] # Pegando apenas o código do setor
    #         float(salario) # Validando se o valor é float.
    #         int(qtdDependentes) # Validando se o valor é int.
    #
    #         if salario == '':
    #             msgAviso = "Campos de sálario precisa ser informado!"
    #             return
    #
    #         conn = Banco.createConnection()
    #
    #         cursor = conn.cursor()
    #         cursor.execute(DataBaseUtils.INSERT_FUNCIONARIO, {
    #             "p1": nome,
    #             "p2": sexo,
    #             "p3": qtdDependentes,
    #             "p4": salario,
    #             "p5": dataAdmissao,
    #             "p6": setorFunc
    #         })
    #         conn.commit()
    #         conn.close()
    #
    #     except ValueError as e:
    #         msgAviso = "Campo de sálario e Qtd de dependentes aceita apenas valores numericos."
    #     except sqlite3.Error as error:
    #         print(error)
    #         msgAviso = "Erro ao acessar o banco de dados."
    #     finally:
    #         Utils.showMsg("Aviso!", msgAviso)
    #
    #     pass
