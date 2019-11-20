# TELA DE LOGIN e SENHA

from tkinter import * #importa todas as blibiotecas do tkinter
from controller.controller_usu import *
from functools import partial

senha = ""
usuario = ""

controller = ControllerLogin()
def btn_click():
   controller.insere(ed1.get(), ed2.get())




janela = Tk()   #Criando a variavel janela que vai reprentara tela 
                # e definindo como tkinter
def btn_login():
   resul = controller.verifica(ed1.get(), ed2.get())

   if resul == True:
      janela.destroy()

# Criando os elementos da tela
lb0 = Label(janela, text="PIZZARIA")
lb1 = Label(janela, text="Login: ")
lb2 = Label(janela, text="Senha: ")
ed1 = Entry(janela,)
ed2 = Entry(janela, show ="*")
bt1 = Button(janela, text="Confirmar")
bt2 = Button(janela, text="Cadastrar")
bt2["command"] = partial(btn_click)
bt1["command"] = partial(btn_login)





#Inserindo so elementos na tela
lb0.grid(row=0, column=0)
lb1.grid(row=1, column=1)
lb2.grid(row=2, column=1)
ed1.grid(row=1, column=2)
ed2.grid(row=2, column=2)
bt1.grid(row=3, column=2, sticky=W)
bt2.grid(row=3, column=2, sticky=E)

#Posição dos elementos
lb0.place(x=125, y=45)
lb1.place(x=50, y=70)
lb2.place(x=50, y=90)
ed1.place(x=100, y=70)
ed2.place(x=100, y=90)
bt1.place(x=100, y=115)
bt2.place(x=170, y=115)


# Tamanho da tela
janela.geometry("300x200+200+200") 
janela.title("Login")
janela.configure(background='#88DDDF')
janela.mainloop()


    