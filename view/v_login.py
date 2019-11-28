# TELA DE LOGIN

from view.v_produtos import *
from view.v_cadastro import *
from controller.controller_usu import *
from functools import partial
from tkinter import *

senha = ""
usuario = ""

controller = ControllerLogin()

#Criando a variavel janela que vai reprentara tela e definindo como tkinter
janela = Tk()

def btn_click():
    tela_teste = tela_cadastro()
    janela.destroy()
    tela_teste.chamaTelaCadastro()
   #controller.insere(ed1.get(), ed2.get())


def btn_login():
   resul = controller.verifica(ed1.get(), ed2.get())

   if resul == True:
      tela2 = tela_produtos()
      janela.destroy()
      tela2.chamaTelaProdutos()

# Logo Pizzaria Top
img = PhotoImage(file="../assets/img/logo.png")
logo = img.subsample(2, 2)
label = Label(janela, image=logo)
label.place(x=0, y=0)

#fonte dos textos
fonte = ('Arial', '16', 'bold')

# Titulo da janela
lb0 = Label(janela, text="LOGIN") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=135)
lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

# Login
lb1 = Label(janela, text="Login: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=35, y=175)
lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
ed1 = Entry(janela, font=fonte) ; ed1.grid(row=1, column=2) ; ed1.place(x=110, y=175)

# Senha
lb2 = Label(janela, text="Senha: ") ; lb2.grid(row=2, column=1) ; lb2.place(x=35, y=215)
lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
ed2 = Entry(janela, font=fonte, show="*") ; ed2.grid(row=2, column=2) ; ed2.place(x=110, y=215)

# Botão Confirmar (1)
bt1 = Button(janela, font=fonte, text="Confirmar", fg="#000000",
             activebackground="#CCCCCC", activeforeground="#FFFFFF")
bt1.grid(row=3, column=3) ; bt1.place(x=150, y=250)

# Botão Cadastrar (2)
bt2 = Button(janela, font=('Arial', '12', 'bold'), text="Cadastrar", fg="#000000",
             activebackground="#CCCCCC", activeforeground="#FFFFFF")
bt2.grid(row=4, column=2) ; bt2.place(x=164, y=300)

bt1["command"] = partial(btn_login)
bt2["command"] = partial(btn_click)

janela.geometry("390x350+200+200")  # largura * altura + x + y
janela.iconbitmap("../assets/img/icone.ico")
janela.title("Pizzaria Top - Login do Usuario")
janela.configure(background='#CCCCCC')
janela.mainloop()
