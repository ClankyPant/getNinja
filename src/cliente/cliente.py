from src.cliente.grupoCliente import GrupoCliente


class Cliente(GrupoCliente):
    __id = None
    __nome = None
    __cnpj_cpf = None
    __telefone = None

    def __init__(self, id, nome, cnpj_cpf, telefone, cod_grupo):
        super().__init__(cod_grupo)
        self.__id = id
        self.__nome = nome
        self.__cnpj_cpf = cnpj_cpf
        self.__telefone = telefone
        pass

    def set_id(self, id):
        self.__id = id
        pass

    def set_nome(self, nome):
        self.__nome = nome
        pass

    def set_cnpj_cpf(self, cnpj_cpf):
        self.__cnpj_cpf = cnpj_cpf
        pass

    def set_telefone(self, telefone):
        self.__telefone = telefone
        pass

    def get_nome(self):
        return self.__nome
        pass

    def get_cnpj_cpf(self):
        return self.__cnpj_cpf
        pass

    def get_telefone(self):
        return self.__telefone
        pass

    def get_id(self):
        return self.__id

    pass
