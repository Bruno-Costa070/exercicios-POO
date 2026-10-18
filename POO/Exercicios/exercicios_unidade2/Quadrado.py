class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_valor):
        self.tamanho_lado = novo_valor

    def retornar_valor(self):
        return self.tamanho_lado

    def calcArea(self):
        return self.tamanho_lado * self.tamanho_lado

terreno_quadrado = Quadrado(40)
print(terreno_quadrado.retornar_valor())
print(terreno_quadrado.calcArea())
terreno_quadrado.mudar_valor_lado(25)
print(terreno_quadrado.calcArea())