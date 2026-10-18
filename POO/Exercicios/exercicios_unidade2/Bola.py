class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor (self, nova_cor):
        self.cor = nova_cor

    def mostraCor (self):
        return self.cor

    def __str__(self):
        return f"Bola de Material: {self.material}\nCor: {self.cor}\nCircunferência {self.circunferencia}cm"

bola_futebol = Bola("branca", 68, "couro")
print(bola_futebol.mostraCor())
bola_futebol.trocaCor("preta")
print(bola_futebol.mostraCor())
print(bola_futebol)