from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class CRUDWindow:
    def OpenCRUD(self):
        window = Tk()
        # - Funções -

        # - __TELA__ -
        # Criando as Abas do CRUD
        abas = ttk.Notebook(window)

        # fonte dos textos
        fonte = ('Arial', '16', 'bold')

        # Colocando a Aba (1) na tela
        aba_create = ttk.Frame(abas)
        # -- Aba Create (1) -- ==========================================================================================
        abas.add(aba_create, text=' (C) Adicionar ')
        # Logo Pizzaria Top
        img11 = PhotoImage(file="../assets/img/logo.png")
        logo11 = img11.subsample(2, 2)
        label11 = Label(aba_create, image=logo11) ; label11.place(x=0, y=0)

        # Titulo da janela
        lb0 = Label(aba_create, text=" Adicionar == Create ") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=140)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Nome
        lb1 = Label(aba_create, text="Nome: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=10, y=175)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(aba_create, font=fonte, width=23) ; ed1.grid(row=1, column=2) ; ed1.place(x=90, y=175)

        # Gasto
        lb3 = Label(aba_create, text="Gasto: R$") ; lb3.grid(row=1, column=1) ; lb3.place(x=10, y=215)
        lb3.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed3 = Entry(aba_create, font=fonte, width=12) ; ed3.grid(row=1, column=2) ; ed3.place(x=120, y=215)

        # Preço
        lb4 = Label(aba_create, text="Preço: R$") ; lb4.grid(row=1, column=1) ; lb4.place(x=10, y=255)
        lb4.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed4 = Entry(aba_create, font=fonte, width=12) ; ed4.grid(row=1, column=2) ; ed4.place(x=120, y=255)

        # Tipo
        lb5 = Label(aba_create, text="Tipo: ") ; lb5.grid(row=1, column=1) ; lb5.place(x=10, y=295)
        lb5.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        combo5 = Combobox(aba_create, font=fonte, state="readonly")
        combo5.grid(row=1, column=1) ; combo5.place(x=75, y=295)
        combo5['values'] = ("Pizza Salgada Grande",
                            "Pizza Salgada Pequena",
                            "Pizza Doce Grande",
                            "Pizza Doce Pequena",
                            "Sucos",
                            "Refrigerantes",
                            "Bebidas Alcoólicas",
                            "Salgados",
                            "Aperitivos")
        combo5.current(0)

        # Validade = ( EM DESENVOLVIMENTO )
        # lb2 = Label(aba_create, text="Validade: ") ; lb2.grid(row=1, column=1) ; lb2.place(x=10, y=330)
        # lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        # ed2 = Entry(aba_create, font=fonte, width=10) ; ed2.grid(row=1, column=2) ; ed2.place(x=120, y=330)

        # Botão Gravar (1)
        btn1 = Button(aba_create, text="Gravar", font=fonte, fg="#24485B", borderwidth=2, relief="solid")
        btn1.grid(row=2, column=1) ; btn1.place(x=150, y=380)
        #bt1["command"] = partial()


        # Colocando a Aba (2) na tela
        aba_read = ttk.Frame(abas)
        # -- Aba Read (2) -- ===========================================================================================
        abas.add(aba_read, text=' (R) Procurar ')
        # Logo Pizzaria Top
        img2 = PhotoImage(file="../assets/img/logo.png")
        logo2 = img2.subsample(2, 2)
        label2 = Label(aba_read, image=logo2) ; label2.place(x=0, y=0)
        # Titulo da janela
        lb0 = Label(aba_read, text=" Procurar == Read ") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=140)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Nome
        lb1 = Label(aba_read, text="Nome: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=10, y=175)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(aba_read, font=fonte, width=23) ; ed1.grid(row=1, column=2) ; ed1.place(x=90, y=175)

        # Tipo
        lb2 = Label(aba_read, text="Tipo: ") ; lb2.grid(row=1, column=1) ; lb2.place(x=10, y=215)
        lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        combo2 = Combobox(aba_read, font=fonte, state="readonly")
        combo2.grid(row=1, column=1) ; combo2.place(x=75, y=215)
        combo2['values'] = ("Pizza Salgada Grande",
                            "Pizza Salgada Pequena",
                            "Pizza Doce Grande",
                            "Pizza Doce Pequena",
                            "Sucos",
                            "Refrigerantes",
                            "Bebidas Alcoólicas",
                            "Salgados",
                            "Aperitivos")
        combo2.current(0)

        # Botão Procurar (2)
        btn2 = Button(aba_read, text="Procurar", font=fonte, fg="#24485B", borderwidth=2, relief="solid")
        btn2.grid(row=2, column=1) ; btn2.place(x=150, y=380)


        # Colocando a Aba (3) na tela
        aba_update = ttk.Frame(abas)
        # -- Aba Update (3) -- =========================================================================================
        abas.add(aba_update, text=' (U) Atualizar ')
        # Logo Pizzaria Top
        img3 = PhotoImage(file="../assets/img/logo.png")
        logo3 = img3.subsample(2, 2)
        label3 = Label(aba_update, image=logo3) ; label3.place(x=0, y=0)
        # Titulo da janela
        lb0 = Label(aba_update, text=" Atualizar == Update ") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=140)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Nome
        lb1 = Label(aba_update, text="Nome: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=10, y=175)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(aba_update, font=fonte, width=23) ; ed1.grid(row=1, column=2) ; ed1.place(x=90, y=175)

        # Gasto
        lb2 = Label(aba_update, text="Gasto: R$");
        lb2.grid(row=1, column=1);
        lb2.place(x=10, y=215)
        lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed2 = Entry(aba_update, font=fonte, width=12);
        ed2.grid(row=1, column=2);
        ed2.place(x=120, y=215)

        # Preço
        lb3 = Label(aba_update, text="Preço: R$") ; lb3.grid(row=1, column=1) ; lb3.place(x=10, y=255)
        lb3.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed3 = Entry(aba_update, font=fonte, width=12) ; ed3.grid(row=1, column=2) ; ed3.place(x=120, y=255)

        # Botão Procurar (3)
        btn3 = Button(aba_update, text="Atualizar", font=fonte, fg="#24485B", borderwidth=2, relief="solid")
        btn3.grid(row=2, column=1) ; btn3.place(x=150, y=380)

        # Colocando a Aba (4) na tela
        aba_delete = ttk.Frame(abas)
        # -- Aba Delete (4) -- =========================================================================================
        abas.add(aba_delete, text=' (D) Apagar ')
        # Logo Pizzaria Top
        img4 = PhotoImage(file="../assets/img/logo.png")
        logo4 = img4.subsample(2, 2)
        label4 = Label(aba_delete, image=logo4) ; label4.place(x=0, y=0)
        # Titulo da janela
        lb0 = Label(aba_delete, text=" Apagar == Delete ") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=140)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Nome
        lb1 = Label(aba_delete, text="Nome: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=10, y=175)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(aba_delete, font=fonte, width=23) ; ed1.grid(row=1, column=2) ; ed1.place(x=90, y=175)

        # Botão Procurar (4)
        btn4 = Button(aba_delete, text="Deletar", font=fonte, fg="#24485B", borderwidth=2, relief="solid")
        btn4.grid(row=2, column=1) ; btn4.place(x=150, y=380)


        # Exibe o notebook na tela usando pack e configura para redimencionar com a janela
        abas.pack(expand=1, fill='both')
        # __ CONFIGURAÇÕES DA TELA __
        window.geometry("390x480+450+100")  # largura * altura + x + y
        window.resizable(width=False, height=False)
        window.iconbitmap("../assets/img/icone.ico")  # icone do cabeçalho da janela
        window.title(" Pizzaria Top - CRUD ")  # texto do cabeçalho da janela
        window.configure(background='#CCCCCC')  # cor de fundo da janela
        window.mainloop()