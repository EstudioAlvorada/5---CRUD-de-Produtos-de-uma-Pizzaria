# TELA DE LOGIN

from tkinter import * ; from tkinter.ttk import *
from controller.controller_usu import *
from functools import partial
from view.v_produtos import *

senha = ""
usuario = ""

controller = ControllerLogin()

def btn_click():
   controller.insere(ed1.get(), ed2.get())

def btn_login():
   resul = controller.verifica(ed1.get(), ed2.get())

   if resul == True:
      tela2 = tela_produtos()
      janela.destroy()
      tela2.chamaTelaProdutos()

#Criando a variavel janela que vai reprentara tela e definindo como tkinter
janela = Tk()

# Logo Pizzaria Top
img = PhotoImage(file="../assets/img/logo.png")
logo = img.subsample(2, 2)
label = Label(janela, image=logo)
label.place(x=0, y=0)

# Criando os elementos da tela ; Inserindo so elementos na tela ; Posição dos elementos

# Titulo
lb0 = Label(janela, text="LOGIN") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=135)
lb0.configure(font="FiraCode 14 bold",
              foreground="#FFFFFF",
              background="#000000",
              width=36)

# Login
lb1 = Label(janela, text="Login: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=50, y=190)
ed1 = Entry(janela,) ; ed1.grid(row=1, column=2) ; ed1.place(x=100, y=190)
# Senha
lb2 = Label(janela, text="Senha: ") ; lb2.grid(row=2, column=1) ; lb2.place(x=50, y=210)
ed2 = Entry(janela, show="*") ; ed2.grid(row=2, column=2) ; ed2.place(x=100, y=210)

bt1 = Button(janela, text="Confirmar") ; bt1.grid(row=3, column=2, sticky=W) ; bt1.place(x=100, y=250)
bt2 = Button(janela, text="Cadastrar") ; bt2.grid(row=3, column=2, sticky=E) ; bt2.place(x=170, y=250)

bt2["command"] = partial(btn_click)
bt1["command"] = partial(btn_login)

janela.geometry("400x300+200+200")
janela.iconbitmap("../assets/img/icone.ico")
janela.title("Pizzaria Top - Login do Usuario")
janela.configure(background='#CCCCCC')
janela.mainloop()
