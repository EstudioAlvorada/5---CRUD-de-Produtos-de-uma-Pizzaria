from tkinter import * ; from tkinter.ttk import *

class tela_produtos:

    def chamaTelaProdutos(self):
        janela = Tk()

        abas = Notebook(janela, width=490, height=290)

        frame_aba1 = Frame(abas)
        frame_aba2 = Frame(abas)
        frame_aba3 = Frame(abas)
        frame_aba4 = Frame(abas)

        label1 = Label(frame_aba1, text="Este é a aba 1")
        label2 = Label(frame_aba2, text="Este é a aba 2")
        label3 = Label(frame_aba3, text="Este é a aba 3")
        label4 = Label(frame_aba4, text="Este é a aba 4")

        label1.grid()
        label2.grid()
        label3.grid()
        label4.grid()

        # CREAT
        abas.add(frame_aba1, text="    *ADICIONAR*    ")
        # READ
        abas.add(frame_aba2, text="    *PROCURAR*    ")
        # UPADTE
        abas.add(frame_aba3, text="    *ATUALIZAR*    ")
        # DELETE
        abas.add(frame_aba4, text="    *APAGAR*    ")

        abas.pack(fill=BOTH, expand=1)

        janela.geometry("400x300+200+200")
        janela.title("CRUD - Produtos")
        janela.mainloop()

