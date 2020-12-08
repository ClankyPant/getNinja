class DescontoFiel():
    __data_primeira_compra = None
    __perc_desconto = float(0)

    def __init__(self, data_primeira_compra):
        self.__data_primeira_compra = data_primeira_compra
    pass

    def get_data_primeira_compra(self):
        return self.__data_primeira_compra
