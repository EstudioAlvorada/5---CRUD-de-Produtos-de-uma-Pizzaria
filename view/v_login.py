# TELA DE LOGIN

from functools import partial
from tkinter import *
<<<<<<< HEAD

senha = ""
usuario = ""

controller = ControllerLogin()

# Criando a variavel janela que vai reprentara tela e definindo como tkinter
janela = Tk()

def btn_login():
   resul = controller.verifica(ed1.get(), ed2.get())
   if resul == True:
      tela2 = tela_produtos()
      janela.destroy()
      tela2.chamaTelaProdutos()


def btn_click():
    tela_teste = tela_cadastro()
    janela.destroy()
    tela_teste.chamaTelaCadastro()
   #controller.insere(ed1.get(), ed2.get())


# __ TELA __
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
lb1 = Label(janela, text="Login: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=15, y=175)
lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
ed1 = Entry(janela, font=fonte, width=30) ; ed1.grid(row=1, column=2) ; ed1.place(x=15, y=205)

# Senha
lb2 = Label(janela, text="Senha: ") ; lb2.grid(row=2, column=1) ; lb2.place(x=15, y=235)
lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
ed2 = Entry(janela, font=fonte, show="*", width=30) ; ed2.grid(row=2, column=2) ; ed2.place(x=15, y=265)

# Botão Confirmar (1)
bt1 = Button(janela, font=fonte, text="Confirmar", fg="#000000",
             activebackground="#CCCCCC", activeforeground="#FFFFFF", width=20)
bt1.grid(row=3, column=3) ; bt1.place(x=65, y=320)
bt1["command"] = partial(btn_login)

# Botão Cadastrar (2)
bt2 = Button(janela, font=('Arial', '12', 'bold'), text="Cadastrar-se", fg="#24485B",
             activebackground="#000000", activeforeground="#FFFFFF", width=15)
bt2.grid(row=4, column=2) ; bt2.place(x=120, y=375)
bt2["command"] = partial(btn_click)

# __ PARAMETROS DA JANELA __
janela.geometry("390x450+200+200")  # largura * altura + x + y
janela.resizable(width=False, height=False)
janela.iconbitmap("../assets/img/icone.ico")  # icone do cabeçalho da janela
janela.title("Pizzaria Top - Login do Usuario")  # texto do cabeçalho da janela
janela.configure(background='#CCCCCC')  # cor de fundo da janela
janela.mainloop()
=======
from view.v_cadastro import Tela_cadastro
from controller.controller_usu import ControllerLogin
from view.v_produtos import tela_produtos


class V_login:
    def abreLogin(self):
        controller = ControllerLogin()

        # Criando a variavel janela que vai reprentara tela e definindo como tkinter
        janela = Tk()

        def btn_login():
           resul = controller.verifica(ed1.get(), ed2.get())
           if resul == True:
              tela2 = tela_produtos()
              janela.destroy()
              tela2.chamaTelaProdutos()


        def btn_click():
            tela_teste = Tela_cadastro()
            janela.destroy()
            tela_teste.chamaTelaCadastro()
           #controller.insere(ed1.get(), ed2.get())


        # __ TELA __
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
        lb1 = Label(janela, text="Login: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=15, y=175)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(janela, font=fonte, width=30) ; ed1.grid(row=1, column=2) ; ed1.place(x=15, y=205)

        # Senha
        lb2 = Label(janela, text="Senha: ") ; lb2.grid(row=2, column=1) ; lb2.place(x=15, y=235)
        lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed2 = Entry(janela, font=fonte, show="*", width=30) ; ed2.grid(row=2, column=2) ; ed2.place(x=15, y=265)

        # Botão Confirmar (1)
        bt1 = Button(janela, font=fonte, text="Confirmar", fg="#000000",
                     activebackground="#CCCCCC", activeforeground="#FFFFFF", width=20)
        bt1.grid(row=3, column=3) ; bt1.place(x=65, y=320)
        bt1["command"] = partial(btn_login)

        # Botão Cadastrar (2)
        bt2 = Button(janela, font=('Arial', '12', 'bold'), text="Cadastrar-se", fg="#24485B",
                     activebackground="#000000", activeforeground="#FFFFFF", width=15)
        bt2.grid(row=4, column=2) ; bt2.place(x=120, y=375)
        bt2["command"] = partial(btn_click)

        # __ PARAMETROS DA JANELA __
        janela.geometry("390x450+200+200")  # largura * altura + x + y
        janela.maxsize(width=390, height=450)  # tamanho maximo
        janela.iconbitmap("../assets/img/icone.ico")  # icone do cabeçalho da janela
        janela.title("Pizzaria Top - Login do Usuario")  # texto do cabeçalho da janela
        janela.configure(background='#CCCCCC')  # cor de fundo da janela
        janela.mainloop()

telaLogin = V_login()
telaLogin.abreLogin()
>>>>>>> 3e9f1149045b8ae5dc3894d3865e4524a638b832
