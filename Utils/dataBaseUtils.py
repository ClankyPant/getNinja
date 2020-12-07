class DataBaseUtils:
    ABSOLUTE_PATH = "D:\\WorkSpacePyCharm\\getNinja\\model\\banco.db"

    CREATE_CLIENTE = """CREATE TABLE IF NOT EXISTS clientes (id integer primary key autoincrement, 
         nome text not null, telefone text, cnpj_cpf String, cod_grupo String);"""

    CREATE_USER = """CREATE TABLE IF NOT EXISTS usuarios (id integer primary key autoincrement, 
        nome text not null, login text not null, senha text not null, isRoot integer);"""

    CREATE_GRUPO = """CREATE TABLE IF NOT EXISTS grupos (id integer primary key autoincrement, 
        codigo Integer not null, nome text not null);"""

    INSERT_USER_ROOT = """INSERT INTO usuarios (id, nome, login, senha, isRoot) 
        values (1, 'admin', 'admin', '123', 1);"""

    INSERT_CLIENTE = """INSERT INTO clientes (nome, cnpj_cpf, telefone, cod_grupo)
                            VALUES (:p1, :p2, :p3, :p4);"""

    INSERT_GRUPO = """INSERT INTO grupos (codigo, nome)
                            VALUES (:p1, :p2);"""

    SELECT_USER_ROOT = "SELECT id FROM usuarios WHERE isRoot = 1"

    SELECT_USER_BY_LOGIN = "SELECT id FROM usuarios WHERE login = :p1 AND senha = :p2"

    SELECT_GRUPOS = """SELECT codigo, nome FROM grupos """

    SELECT_CLIENTE_BY_ID = """SELECT NOME, TELEFONE, CNPJ_CPF, COD_GRUPO FROM CLIENTES WHERE ID = :p1"""

    SELECT_ALL_CLIENTES = """SELECT ID, NOME, TELEFONE, CNPJ_CPF, COD_GRUPO FROM CLIENTES"""

    UPDATE_CLIENTE_BY_ID = """UPDATE CLIENTES SET NOME = :p1, TELEFONE = :p2, CNPJ_CPF = :p3, COD_GRUPO = :p4  
                            WHERE ID = 7 """

    DELETE_CLIENTE = "DELETE FROM clientes WHERE id = :p1"