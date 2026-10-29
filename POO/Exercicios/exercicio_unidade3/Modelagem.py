class Amigo:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = []

    def insereTelefone(self, telefone):
        self.telefones.append(telefone)

    def listaTelefones(self):
        for telefone in self.telefones:
            print(telefone.numero)

class Telefone:
    def __init__(self, numero):
        self.numero = numero

amigo1 = Amigo('Gabriel')
amigo1.insereTelefone(Telefone(84305215))
amigo1.insereTelefone(Telefone(97523510))
(amigo1.listaTelefones())