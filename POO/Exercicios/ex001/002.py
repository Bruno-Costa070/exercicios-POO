class Calculadora:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def soma(self):
    return self.x + self.y

   def sub(self):
     return self.x - self.y

calc = Calculadora(4,5)
print(calc.soma())

calc = Calculadora(5,3)
print(calc.sub())