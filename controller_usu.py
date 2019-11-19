from conexao import ConectaBanco

class ControllerLogin():

    def insere(self,usuario,senha):
        banco = ConectaBanco()
        banco.verificaUsuario(usuario,senha)
        