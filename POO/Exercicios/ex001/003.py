class Calculadora:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.operacoes = ['soma', 'subtração']

    def soma(self):
        return self.x + self.y

    def subtracao(self):
        return self.x - self.y

calc = Calculadora()
calc.x = 5
calc.y = 3
print(calc.soma())
print(calc.subtracao())

print(calc.operacoes)

calc.nome = 'Minha Calculadora'

print(calc.nome)