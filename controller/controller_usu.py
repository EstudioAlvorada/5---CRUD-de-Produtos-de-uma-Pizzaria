from model.conexao import ConectaBanco

class ControllerLogin():

    def insere(self, usuario, senha):
        banco = ConectaBanco()
        banco.insereUsuario(usuario, senha)



    def verifica(self, usuario, senha):
        banco = ConectaBanco()
        resultado = banco.verificaUsuario(usuario, senha)
        return resultado
        