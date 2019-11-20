from model.conexao import ConectaBanco

class ControllerLogin():

    def insere(self, usuario, senha):
        banco = ConectaBanco()
        banco.insereUsuario(usuario, senha)


    def verifica(self, usuario, senha):
        banco = ConectaBanco()
        banco.verificaUsuario(usuario, senha)
        