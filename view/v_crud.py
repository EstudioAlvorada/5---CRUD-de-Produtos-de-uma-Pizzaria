from tkinter import *
from tkinter import ttk

class CRUDWindow:
    def OpenCRUD(self):
        window = Tk()

        # Criando as Abas do CRUD
        abas = ttk.Notebook(window)

        # fonte dos textos
        fonte = ('Arial', '16', 'bold')

        # Colocando a Aba (1) na tela
        aba_creat = ttk.Frame(abas)
        # -- Aba Creat (1) -- ==========================================================================================
        abas.add(aba_creat, text=' (C) Adicionar ')
        # Logo Pizzaria Top
        img1 = PhotoImage(file="../assets/img/logo.png")
        logo1 = img1.subsample(2, 2)
        label1 = Label(aba_creat, image=logo1) ; label1.place(x=0, y=0)
        # Titulo da janela
        lb1 = Label(aba_creat, text=" Adicionar == Creat ") ; lb1.grid(row=0, column=0) ; lb1.place(x=0, y=140)
        lb1.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Colocando a Aba (2) na tela
        aba_read = ttk.Frame(abas)
        # -- Aba Read (2) -- ===========================================================================================
        abas.add(aba_read, text=' (R) Procurar ')
        # Logo Pizzaria Top
        img2 = PhotoImage(file="../assets/img/logo.png")
        logo2 = img2.subsample(2, 2)
        label2 = Label(aba_read, image=logo2) ; label2.place(x=0, y=0)
        # Titulo da janela
        lb2 = Label(aba_read, text=" Procurar == Read ") ; lb2.grid(row=0, column=0) ; lb2.place(x=0, y=140)
        lb2.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Colocando a Aba (3) na tela
        aba_update = ttk.Frame(abas)
        # -- Aba Update (3) -- =========================================================================================
        abas.add(aba_update, text=' (U) Atualizar ')
        # Logo Pizzaria Top
        img3 = PhotoImage(file="../assets/img/logo.png")
        logo3 = img3.subsample(2, 2)
        label3 = Label(aba_update, image=logo3) ; label3.place(x=0, y=0)
        # Titulo da janela
        lb3 = Label(aba_update, text=" Atualizar == Update ") ; lb3.grid(row=0, column=0) ; lb3.place(x=0, y=140)
        lb3.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Colocando a Aba (4) na tela
        aba_delete = ttk.Frame(abas)
        # -- Aba Delete (4) -- =========================================================================================
        abas.add(aba_delete, text=' (D) Apagar ')
        # Logo Pizzaria Top
        img4 = PhotoImage(file="../assets/img/logo.png")
        logo4 = img4.subsample(2, 2)
        label4 = Label(aba_delete, image=logo4) ; label4.place(x=0, y=0)
        # Titulo da janela
        lb4 = Label(aba_delete, text=" Apagar == Delete ") ; lb4.grid(row=0, column=0) ; lb4.place(x=0, y=140)
        lb4.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Exibe o notebook na tela usando pack e configura para redimencionar com a janela
        abas.pack(expand=1, fill='both')
        # __ CONFIGURAÇÕES DA TELA __
        window.geometry("390x480+200+200")  # largura * altura + x + y
        window.resizable(width=False, height=False)
        window.iconbitmap("../assets/img/icone.ico")  # icone do cabeçalho da janela
        window.title(" Pizzaria Top - CRUD ")  # texto do cabeçalho da janela
        window.configure(background='#CCCCCC')  # cor de fundo da janela
        window.mainloop()