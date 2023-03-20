
class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def alterar_canal(self, novo_canal):
        if novo_canal < 1 or novo_canal > 100:
            print('Canal Inválido')
        else:
            self.canal = novo_canal

    def alterar_volume(self, novo_volume):
        if novo_volume < 0 or novo_volume > 100:
            print('Volume Inválido')
        else:
            self.volume = novo_volume


tv = TV()
tv.alterar_canal(50)
print(f'Canal Atual: {tv.canal}')
tv.alterar_volume(80)
print(f'Volume Atual: {tv.volume}')
tv.alterar_canal(150)
tv.alterar_volume(-10)
