from tkinter import *

class tela_read:
    def chamaTelaRead(self):
        janela = Tk()

        # __ TELA __
        # Logo Pizzaria Top
        img = PhotoImage(file="../assets/img/logo.png")
        logo = img.subsample(2, 2)
        label = Label(janela, image=logo)
        label.place(x=0, y=0)

        # fonte dos textos
        fonte = ('Arial', '16', 'bold')

        # Titulo da janela
        lb0 = Label(janela, text="Read - Procurar") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=135)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # __ PARAMETROS DA JANELA __
        janela.geometry("390x450+200+200")
        janela.maxsize(width=390, height=450)
        janela.iconbitmap("../assets/img/icone.ico")
        janela.title("Pizzaria Top - CRUD Produtos - Procurar")
        janela.configure(background='#CCCCCC')
        janela.mainloop()