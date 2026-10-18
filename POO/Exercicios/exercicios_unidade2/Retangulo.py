class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornar_valores(self):
        return self.base, self.altura

    def calcArea(self):
        return self.base * self.altura

    def calcPerimetro(self):
        return 2 * (self.base + self.altura)

predio = Retangulo(30, 70)
print(predio.retornar_valores())
print(predio.calcArea())
print(predio.calcPerimetro())
predio.mudar_valor_lados(10, 50)
print(predio.calcArea())
print(predio.calcPerimetro())