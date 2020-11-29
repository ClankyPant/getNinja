class DataBaseUtils:
    ABSOLUTE_PATH = "/home/luis/workspacePy/getNinja/model/banco.db"

    CREATE_FUNCIONARIO = """CREATE TABLE IF NOT EXISTS funcionarios (id_funcionario integer primary key autoincrement, 
        nome text not null, sexo text, data_nascimento text, qtd_dependentes integer, cargo text, salario integer, 
        setor text); """

    CREATE_USER = """CREATE TABLE IF NOT EXISTS usuarios (user_id integer primary key autoincrement, 
        nome text not null, login text not null, senha text not null, isRoot integer);"""

    INSERT_USER_ROOT = """INSERT INTO usuarios (user_id, nome, login, senha, isRoot) 
        values (1, 'admin', 'admin', '123', 1);"""

    SELECT_USER_ROOT = "SELECT user_id FROM usuarios WHERE isRoot = 1"

    SELECT_USER_BY_LOGIN = "SELECT user_id FROM usuarios WHERE login = :p1 AND senha = :p2"