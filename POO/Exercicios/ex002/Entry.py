from tkinter import *
class App:
   def __init__(self):
    self.janela = Tk()

    #Container 1
    self.frame1 = Frame(self.janela)
    self.frame1.pack()

    #Linha de texto
    self.texto1 = Label(self.frame1, text='Nome: ')
    #Colocando a linha de texto do lado esquerdo
    self.texto1.pack(side = LEFT)

    #Caixa de texto para receber valores
    self.caixa1 = Entry(self.frame1)
    #Colocando a caixa no lado direito
    self.caixa1.pack(side = RIGHT)

    #Container 2
    self.frame2 = Frame(self.janela)
    self.frame2.pack()

    #Linha de texto
    self.texto2 = Label(self.frame2, text='Telefone: ')
    #Colocando o texto da lado esquerdo
    self.texto2.pack(side = LEFT)

    #Caixa de texto para receber valores
    self.caixa2 = Entry(self.frame2)
    #Colocando a caixa do lado direito
    self.caixa2.pack(side = RIGHT)

    self.janela.mainloop()

aplicacao=App()
