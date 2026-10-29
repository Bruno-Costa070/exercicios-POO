from tkinter import *
class App:
   def __init__(self):
    self.janela = Tk()

    self.frame1 = Frame(self.janela)
    self.frame1.pack()

    #Botão a esquerda
    self.botao1 = Button(self.frame1, text='B1')
    self.botao1.pack(side = LEFT)

    #Botão a esquerda
    self.botao2 = Button(self.frame1, text='B2')
    self.botao2.pack(side = LEFT)

    #Botão a esquerda
    self.botao3 = Button(self.frame1, text='B3')
    self.botao3.pack(side = RIGHT)

    #Botão em baixo
    self.frame2 = Frame(self.janela)
    self.frame2.pack(side=BOTTOM)

    #Botão no topo
    self.botao4 = Button(self.frame2, text='B4')
    self.botao4.pack()

    self.janela.mainloop()

aplicacao=App()