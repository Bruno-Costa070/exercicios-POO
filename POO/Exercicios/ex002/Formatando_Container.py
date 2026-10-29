from tkinter import *
class App:
   def __init__(self):
    self.janela = Tk()

    self.frame1 = Frame(self.janela)
    self.frame1['bg']='blue'

     #Configurando o container 1 (frame1)
    self.frame1['height']=50
    self.frame1['width']=400

    #Configurando o container 2 (frame2)
    self.frame2 = Frame(self.janela)
    self.frame2['bg']='green'
    self.frame2['height']=100
    self.frame2['width']=300

    self.frame1.pack()
    self.frame2.pack()

    self.janela.mainloop()

aplicacao=App()
