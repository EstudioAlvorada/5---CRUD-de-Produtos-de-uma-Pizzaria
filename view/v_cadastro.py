from tkinter import * ; from tkinter.ttk import *
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
        # img = PhotoImage(file="../assets/img/logo.png")
        # logo = img.subsample(2, 2)
        # label = Label(janela, image=logo)
        # label.place(x=0, y=0)

        # Criando os elementos da tela ; Inserindo so elementos na tela ; Posição dos elementos

        # Titulo
        lb0 = Label(janela, text="CADASTRO");
        lb0.grid(row=0, column=0);
        lb0.place(x=0, y=135)
        lb0.configure(font="Arial 14 bold",
                      foreground="#FFFFFF",
                      background="#000000",
                      width=50)

        # Login
        lb1 = Label(janela, text="Login: ");
        lb1.grid(row=1, column=1);
        lb1.place(x=45, y=170)
        lb1.configure(font="Arial 14 bold",
                      foreground="#000000",
                      background="#CCCCCC")
        ed1 = Entry(janela, );
        ed1.grid(row=1, column=2);
        ed1.place(x=115, y=175)
        # Senha
        lb2 = Label(janela, text="Senha: ");
        lb2.grid(row=2, column=1);
        lb2.place(x=45, y=210)
        lb2.configure(font="Arial 14 bold",
                      foreground="#000000",
                      background="#CCCCCC")
        ed2 = Entry(janela, show="*");
        ed2.grid(row=2, column=2);
        ed2.place(x=115, y=215)

        lb3 = Label(janela, text="Confirmar Senha: ");
        lb3.grid(row=3, column=2);
        lb3.place(x=45, y=250)
        lb3.configure(font="Arial 14 bold",
                      foreground="#000000",
                      background="#CCCCCC")
        ed3 = Entry(janela, show="*");
        ed3.grid(row=3, column=3);
        ed3.place(x=220, y=255)

        lb4 = Label(janela, text="Nome Completo: ");
        lb4.grid(row=3, column=2);
        lb4.place(x=45, y=290)
        lb4.configure(font="Arial 14 bold",
                      foreground="#000000",
                      background="#CCCCCC")
        ed4 = Entry(janela);
        ed4.grid(row=3, column=3);
        ed4.place(x=220, y=295)

        bt1 = Button(janela, text="Cadastrar");
        bt1.grid(row=3, column=2, sticky=W);
        bt1.place(x=105, y=370)

        bt1["command"] = partial(cadastra)


        janela.geometry("500x400+200+200")
        janela.iconbitmap("../assets/img/icone.ico")
        janela.title("Pizzaria Top - Cadastro de Usuario")
        janela.mainloop()