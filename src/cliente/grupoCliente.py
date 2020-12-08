class GrupoCliente:
    __cod_grupo = None
    __nome_grupo = None
    __cod_cliente_pai = None

    def __init__(self, cod_grupo, nome_grupo, cod_cliente_pai):
        self.__cod_grupo = cod_grupo
        self.__nome_grupo = nome_grupo
        self.__cod_cliente_pai = cod_cliente_pai
        pass

    def set_cod_grupo(self, cod_grupo):
        self.__cod_grupo = cod_grupo
        pass

    def set_nome_grupo(self, nome_grupo):
        self.__nome_grupo = nome_grupo
        pass

    def set_cod_cliente_pai(self, cod_cliente_pai):
        self.__cod_cliente_pai = cod_cliente_pai
        pass

    def get_cod_grupo(self):
        return self.__cod_grupo

    def get_nome_gropo(self):
        return self.__nome_grupo

    def get_cod_Cliente_Pai(self):
        return self.__cod_cliente_pai