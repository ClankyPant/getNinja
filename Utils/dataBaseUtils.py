class DataBaseUtils:
    ABSOLUTE_PATH = "D:\\WorkSpacePyCharm\\getNinja\\model\\banco.db"

    CREATE_FUNCIONARIO = """CREATE TABLE IF NOT EXISTS funcionarios (id integer primary key autoincrement, 
         nome text not null, cnpjCpf text, dataFundacao date, cargo text, salario double);"""

    CREATE_USER = """CREATE TABLE IF NOT EXISTS usuarios (id integer primary key autoincrement, 
        nome text not null, login text not null, senha text not null, isRoot integer);"""

    INSERT_USER_ROOT = """INSERT INTO usuarios (id, nome, login, senha, isRoot) 
        values (1, 'admin', 'admin', '123', 1);"""

    INSERT_FUNCIONARIO = """INSERT INTO funcionarios (nome, cnpjCpf, dataFundacao, cargo, salario)
                            VALUES (:p1, :p2, :p3, :p4, :p5);"""

    SELECT_USER_ROOT = "SELECT id FROM usuarios WHERE isRoot = 1"

    SELECT_USER_BY_LOGIN = "SELECT id FROM usuarios WHERE login = :p1 AND senha = :p2"