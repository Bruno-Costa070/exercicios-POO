from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.botao1 = Button(self.frame1, text='Ok')

        #Cor do botão
        self.botao1['bg']='red'

        #Altura do botão
        self.botao1['height']=3

        #Largura do botão
        self.botao1['width']=10

        #Fonte do botão
        self.botao1['font']=('Verdana', '12', 'bold', 'italic')

        #Cor do texto do botão
        self.botao1['fg']='black'

        self.botao1.pack()

        self.janela.mainloop()

aplicacao=App()