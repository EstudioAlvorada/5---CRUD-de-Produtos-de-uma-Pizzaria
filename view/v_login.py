# TELA DE LOGIN e SENHA
from controller.controller_login import Controller_Login
from tkinter import * #importa todas as blibiotecas do tkinter
from functools import partial

janela = Tk()   #Criando a variavel janela que vai reprentara tela 
                # e definindo como tkinter




# Criando os elementos da tela
lb_logo = Label(janela, text="PIZZARIA")
lb_login = Label(janela, text="Login: ")
lb_senha = Label(janela, text="Senha: ")
ed_login = Entry(janela,)
ed_senha = Entry(janela,)
bt_conf = Button(janela, text="Confirmar")
bt_cad = Button(janela, text="Cadastrar")

#Inserindo so elementos na tela
lb_logo.grid(row=0, column=0)
lb_login.grid(row=1, column=1)
lb_senha.grid(row=2, column=1)
ed_login.grid(row=1, column=2)
ed_senha.grid(row=2, column=2)
bt_conf.grid(row=3, column=2, sticky=W)
bt_cad.grid(row=3, column=2, sticky=E)


#Posição dos elementos
lb_logo.place(x=125, y=45)
lb_login.place(x=50, y=70)
lb_senha.place(x=50, y=90)
ed_login.place(x=100, y=70)
ed_senha.place(x=100, y=90)
bt_conf.place(x=100, y=115)
bt_cad.place(x=170, y=115)

# Tamanho da tela
janela.geometry("300x200+200+200") # tamanho da janela
janela.title("Login") # titulo da janela
#janela.configure(background='#88DDDF')
#janela.configure(background= "assets/img/bannerpizza-01.png") # background da janela
janela.iconbitmap("assets/img/icone.ico") # icone da janela
janela.mainloop()


    