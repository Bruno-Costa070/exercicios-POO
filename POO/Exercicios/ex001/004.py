class Pessoa:
    __nome = None

    def __init__(self):
        pass

    def setnome(self, valor):
        self.__nome = valor

    def getnome(self):
        return self.__nome

bruno = Pessoa()

#O nome foi salvo como Bruno 
bruno.setnome("Bruno")

#O nome foi definindo como sendo a variável nome_atual
nome_atual = bruno.getnome()

#o nome "Bruno" foi printado na tela
print(nome_atual)