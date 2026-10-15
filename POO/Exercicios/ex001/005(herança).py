class ClasseA:
    m3 = 3
    m4 = 4

class ClasseB(ClasseA):
    m1 = 1
    m2 = 2

a = ClasseB()

print(a.m1)
print(a.m2)
print(a.m3)
print(a.m4)


#Subclasse herdando método contrutor da Superclasse
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

        
gato = Gato("Tom")
gato.comer()

class Classe1:
    def ver(self):
        print('Estou na Classe 1')

class Classe2:
    def mostrar(self):
        print('Estou na Classe 2')

class Classe3(Classe1, Classe2):
    def exibir(self):
        print('Estou na Classe 3')

teste = Classe3()
teste.ver()
teste.mostrar()
teste.exibir()