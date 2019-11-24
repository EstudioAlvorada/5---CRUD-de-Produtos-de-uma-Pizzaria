from tkinter import * ; from tkinter.ttk import *

class tela_cadastro:

    def chamaTelaCadastro(self):
        janela = Tk()

        janela.geometry("400x300+200+200")
        janela.iconbitmap("../assets/img/icone.ico")
        janela.title("Pizzaria Top - Cadastro de Usuario")
        janela.mainloop()