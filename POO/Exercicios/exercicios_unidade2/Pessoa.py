class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
            self.idade += anos
            if self.idade < 21:
               self.altura += 0.5

    def engordar(self, peso):
         self.peso += peso

    def emagrecer(self, peso):
         self.peso -= peso

    def crescer(self, centimetros):
         self.altura += centimetros

humano = Pessoa("Bruno", 20, 75, 1.75)
humano.envelhecer(1)
print("idade após envelhecer:", humano.idade)
print("Altura após envelhecer:", humano.altura)

humano.emagrecer(3)
print("Peso após emagrecer:", humano.peso)