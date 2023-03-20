
from rich import print


class Bola:
    def __init__(self, cor, circunferencia, material):
        try:
            self.cor = cor
            self.circunferencia = circunferencia
            self.material = material
        except ValueError:
            print('[red]ERRO. Um ou mais argumentos inválidos[/]')

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}')


bola = Bola('verde', 20, 'couro')
bola.mostra_cor()
bola.troca_cor('azul')
bola.mostra_cor()
