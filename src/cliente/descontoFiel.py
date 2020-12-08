import datetime
import pandas


class DescontoFiel():
    __data_primeira_compra = None

    def __init__(self, data_primeira_compra):
        self.__data_primeira_compra = data_primeira_compra
    pass

    def get_data_primeira_compra(self):
        return self.__data_primeira_compra

    def get_perc_desconto(self):
        perc_desconto = float(0.0)
        listDate = str(self.get_data_primeira_compra()).split('/')
        if pandas.notnull(listDate[2]):
            ano_primeira_compra = listDate[2]
            qtd_anos_fiel = int(datetime.datetime.today().year) - int(ano_primeira_compra)

            if qtd_anos_fiel > 1:
                perc_desconto = 10
                qtd_anos_fiel -= 1
                if qtd_anos_fiel >= 1:
                    perc_desconto += (0.01 * qtd_anos_fiel) * 100

        return str(perc_desconto)

    def set_data_primeira_compra(self, data_primeira_compra):
        self.__data_primeira_compra = data_primeira_compra
        pass

    pass
