from tkinter import *
class App:
   def __init__(self):
    self.janela = Tk()
    
    self.frame1 = Frame(self.janela)
    self.frame1.pack()

    #Label insere um texto em uma linha única
    self.texto1 = Label(self.frame1)
    self.texto1['text']='Roberto Carlos'

    self.texto1['bg']='black'

    self.texto1['fg']='white'

    self.texto1['font']=('Arial','20','bold')

    self.texto1.pack()

    self.janela.mainloop()

aplicacao=App()
