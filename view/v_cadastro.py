from tkinter import *
from controller.controller_usu import *
from functools import partial

class tela_cadastro:

    def chamaTelaCadastro(self):
        janela = Tk()

        def cadastra():
            controller = ControllerLogin()

            if ed2.get() == ed3.get():
                controller.insere(ed1.get(), ed2.get(), ed4.get())
            else:
                print("senhas diferentes")


        # Logo Pizzaria Top
        img = PhotoImage(file="../assets/img/logo.png")
        logo = img.subsample(2, 2)
        label = Label(janela, image=logo)
        label.place(x=0, y=0)

        # fonte dos textos
        fonte = ('Arial', '16', 'bold')

        # Titulo da janela
        lb0 = Label(janela, text="CADASTRO") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=135)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # FORMULARIO DE CADASTRO

        # Nome Completo
        lb1 = Label(janela, text="Nome Completo: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=10, y=170)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(janela, font=fonte, width=30) ; ed1.grid(row=2, column=1) ; ed1.place(x=10, y=200)

        # Login
        lb2 = Label(janela, text="Login: "); lb2.grid(row=3, column=1); lb2.place(x=10, y=230)
        lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed2 = Entry(janela, font=fonte, width=30) ; ed2.grid(row=4, column=2) ; ed2.place(x=10, y=260)

        # Senha
        #lb3 = Label(janela, text="Senha: ") ; lb3.grid(row=5, column=1) ; lb3.place(x=10, y=250)
        #lb3.configure(font="Arial 14 bold", foreground="#000000", background="#CCCCCC")
        #ed3 = Entry(janela, font=fonte, show="*", width=16) ; ed3.grid(row=6, column=1) ; ed3.place(x=80, y=250)

        # Confirmar Senha
        #lb4 = Label(janela, text="Confirmar Senha: ") ; lb4.grid(row=4, column=2) ; lb4.place(x=45, y=250)
        #lb4.configure(font="Arial 14 bold", foreground="#000000", background="#CCCCCC")
        #ed4 = Entry(janela, show="*") ; ed4.grid(row=3, column=3) ; ed3.place(x=220, y=255)

        # Botão Cadastrar (1)
        bt1 = Button(janela, text="Cadastrar") ; bt1.grid(row=3, column=2) ; bt1.place(x=105, y=370)

        bt1["command"] = partial(cadastra)

        janela.geometry("390x400+200+200")
        janela.iconbitmap("../assets/img/icone.ico")
        janela.title("Pizzaria Top - Cadastro de Usuario")
        janela.configure(background='#CCCCCC')
        janela.mainloop()