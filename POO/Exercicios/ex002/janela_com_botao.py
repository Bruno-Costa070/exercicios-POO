from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()

        #Container (frame1) dentro da janela (self.janela)
        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        #Inserindo um botão (botao1) dentro do container (frame1)
        self.botao1 = Button(self.frame1, text='Ok')
        self.botao1['bg']='red'
        self.botao1.pack()

        self.janela.mainloop()

aplicacao=App()