from tkinter import *
class App:
   def __init__(self):
        self.janela = Tk()

        #Nome da Janela(Título)
        self.janela.title('Janela Internacional')

        #Dimensões da Janela
        self.janela.geometry('600x300')

        self.janela.mainloop()

aplicacao=App()