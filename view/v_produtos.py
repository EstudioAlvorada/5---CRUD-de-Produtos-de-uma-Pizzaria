from view.v_creat import *
from view.v_read import *
from view.v_update import *
from view.v_delete import *
from functools import partial
from tkinter import *

class tela_produtos:
    def chamaTelaProdutos(self):
        janela = Tk()
        def btn_creat():
            tela_c = tela_creat()
            janela.destroy()
            tela_c.chamaTelaCreat()


        def btn_read():
            tela_r = tela_read()
            janela.destroy()
            tela_r.chamaTelaRead()


        def btn_update():
            tela_u = tela_update()
            janela.destroy()
            tela_u.chamaTelaUpdate()


        def btn_delete():
            tela_d = tela_delete()
            janela.destroy()
            tela_d.chamaTelaDelete()


        # __ TELA __
        # Logo Pizzaria Top
        img = PhotoImage(file="../assets/img/logo.png")
        logo = img.subsample(2, 2)
        label = Label(janela, image=logo)
        label.place(x=0, y=0)

        # fonte dos textos
        fonte = ('Arial', '16', 'bold')

        # Titulo da janela
        lb0 = Label(janela, text="CRUD - PRODUTOS") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=135)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        lb1 = Label(janela, text="Escolha uma das opções do C.R.U.D. ") ; lb1.grid(row=1, column=1) ; lb1.place(x=5, y=180)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")

        # CREAT - Botão Adicionar (1)
        bt1 = Button(janela, font=fonte, text="Adicionar", fg="#000000",
                     activebackground="#CCCCCC", activeforeground="#FFFFFF", width=10)
        bt1.grid(row=2, column=3) ; bt1.place(x=35, y=225)
        bt1["command"] = partial(btn_creat)

        # READ - Botão Procurar (2)
        bt2 = Button(janela, font=fonte, text="Procurar", fg="#000000",
                     activebackground="#CCCCCC", activeforeground="#FFFFFF", width=10)
        bt2.grid(row=2, column=4) ; bt2.place(x=215, y=225)
        bt2["command"] = partial(btn_read)

        # UPADTE - Botão Atualizar (3)
        bt3 = Button(janela, font=fonte, text="Atualizar", fg="#000000",
                     activebackground="#CCCCCC", activeforeground="#FFFFFF", width=10)
        bt3.grid(row=3, column=3) ; bt3.place(x=35, y=295)
        bt3["command"] = partial(btn_update)

        # DELETE - Botão Apagar (4)
        bt4 = Button(janela, font=fonte, text="Apagar", fg="#000000",
                     activebackground="#CCCCCC", activeforeground="#FFFFFF", width=10)
        bt4.grid(row=3, column=4) ; bt4.place(x=215, y=295)
        bt4["command"] = partial(btn_delete)
        # Botão Voltar (5)
        bt5 = Button(janela, font=fonte, text="<< Voltar", fg="#E8252D",
                     activebackground="#000000", activeforeground="#FFFFFF", width=10)
        bt5.grid(row=4, column=3) ; bt5.place(x=130, y=355)

        # __ PARAMETROS DA JANELA __
        janela.geometry("390x450+200+200")
        janela.maxsize(width=390, height=450)
        janela.iconbitmap("../assets/img/icone.ico")
        janela.title("Pizzaria Top - CRUD Produtos")
        janela.configure(background='#CCCCCC')
        janela.mainloop()

