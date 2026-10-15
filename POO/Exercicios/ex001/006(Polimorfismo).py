class Animal:
    quemsou = 'Sou um Animal'
    def som(self):
        return 'Som genérico'

class Gato(Animal):
    def som(self):
        return 'Miau'

class Cachorro(Animal):
    def som(self):
        return 'Auau'

bicho_01 = Animal()
print(f'{bicho_01.quemsou} {bicho_01.som()}')

bicho_02 = Gato()
print(f'{bicho_02.quemsou} {bicho_02.som()}')

bicho_03 = Cachorro()
print(f'{bicho_03.quemsou} {bicho_03.som()}')