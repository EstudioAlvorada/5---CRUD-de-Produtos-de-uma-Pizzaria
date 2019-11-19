from model.conexao import ConectaBanco

class Controller_Login:

    def login_controller(self,usuario,senha):
        resultado = ConectaBanco.verificaUsuario(self,usuario, senha)
        return resultado


