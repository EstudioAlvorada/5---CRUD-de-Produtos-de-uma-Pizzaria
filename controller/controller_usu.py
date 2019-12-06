from model.conexao import ConectaBanco


class ControllerLogin():
    def insere(self, usuario, senha, nome):
        banco = ConectaBanco()
        banco.insereUsuario(usuario, senha, nome)

    def verifica(self, *args):
        banco = ConectaBanco()
        resultado = banco.verificaUsuario(*args)
        return resultado


class Controllercrud():
    def armazenaUsuario(self):
        banco = ConectaBanco()


    def criar(self, nomeP, gastoP, precoP):
        teste = ConectaBanco()
        teste.adicionar(nomeP, gastoP, precoP)


    #def ler(self):
    #def atualizar(self):
    #def deletar(self):
