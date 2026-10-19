class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 20

    def mudarCanal(self, novo_canal):
        self.canal = novo_canal
        if self.canal > 300 or self.canal < 1:
            self.canal = 1

    def aumentarVolume(self, aumentar):
        self.volume += aumentar
        if self.volume > 100:
            self.volume = 100

    def diminuirVolume(self, diminuir):
        self.volume -= diminuir
        if self.volume < 0:
            self.volume = 0

Televisao = TV()
Televisao.mudarCanal(104)
print("Canal Atual:", Televisao.canal)

Televisao.aumentarVolume(35)
print("Volume:", Televisao.volume)
Televisao.diminuirVolume(10)
print("Volume:", Televisao.volume)