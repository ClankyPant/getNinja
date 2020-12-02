class ClienteModel:
    __nome = None
    __cnpj_cpf = None
    __telefone = None
    __data_primeira_compra = None
    __data_ult_compra = None
    __cod_grupo = None

    def __init__(self, nome, cnpj_cpf, telefone, cod_grupo):
        self.set_nome(nome)
        self.set_cnpj_cpf(cnpj_cpf)
        self.set_telefone(telefone)
        self.set_cod_grupo(cod_grupo)
        pass
    
    def set_nome(self, nome):
        self.nome = nome
        pass

    def set_cnpj_cpf(self, cnpj_cpf):
        self.cnpj_cpf = cnpj_cpf
        pass

    def set_telefone(self, telefone):
        self.telefone = telefone
        pass

    def set_data_primeira_compra(self, data_primeira_compra):
        self.data_primeira_compra = data_primeira_compra
        pass

    def set_data_ult_compra(self, data_ult_compra):
        self.data_ult_compra = data_ult_compra
        pass

    def set_cod_grupo(self, cod_grupo):
        self.cod_grupo = cod_grupo
        pass

    def get_nome(self):
        return self.nome
        pass

    def get_cnpj_cpf(self):
        return self.cnpj_cpf
        pass

    def get_telefone(self):
        return self.telefone
        pass

    def get_data_primeira_compra(self):
        return self.data_primeira_compra
        pass

    def get_data_ult_compra(self):
        return self.data_ult_compra
        pass

    def get_cod_grupo(self):
        return self.cod_grupo
        pass
