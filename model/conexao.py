import MySQLdb  # Importa a biblioteca do MySQL


class ConectaBanco:  # Define a classe
    def __init__(self):  # init é o metodo inicializador da classe

        self.con = ""  # Cria a variavel de conexão vazia

    def conecta(self):  # Método para conectar no banco
        host = "localhost"  # Nome utilizado no host no Workbenck
        user = "root"  # Nome do usuario que criamos no Workbenck
        password = ""  # Senha que colocamos para o usuario
        db = "produtos_pizzaria"  # Nome do banco de dados
        port = 3306  # Porta configurada para o server MySQL
        self.con = MySQLdb.connect(host, user, password, db, port)  # Na variavel con cria nossa conexão

    def insereUsuario(self, usuario, senha, nome):
        self.conecta()
        cur = self.con.cursor()

        query = (
                'insert into tbl_usuarios (login_usuario, senha_usuario, nome_usuario)values ("{}", "{}", "{}");'.format(
                    usuario, senha, nome))

        cur.execute(query)

        self.con.commit()
        self.con.close()

        # if cur.rowcount > 0:
        #     result = True
        # else:
        #     result = False

        # return result

    def verificaUsuario(self, usuario, senha):
        self.conecta()
        cur = self.con.cursor()

        query = (
            "select login_usuario, senha_usuario from tbl_usuarios where login_usuario = '{}' and senha_usuario = '{}';".format(
                usuario, senha))
        cur.execute(query)

        resultado = cur.fetchall()

        if len(resultado) > 0:
            return True
        else:
            return False
