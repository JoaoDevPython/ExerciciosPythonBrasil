
from rich import print


class Quadrado:
    def __init__(self, lado):
        try:
            self.lado = lado
        except ValueError:
            print('[red]ERRO. O valor de lado precisa ser um número[/]')

    def muda_lado(self, novo_lado):
        self.lado = novo_lado

    def retorna_lado(self):
        return self.lado

    def calcula_area(self):
        return pow(self.lado, 2)


quadrado = Quadrado(5)
print(f'{quadrado.retorna_lado()}\n'
      f'{quadrado.calcula_area()}')
quadrado.muda_lado(10)
print(f'{quadrado.retorna_lado()}\n'
      f'{quadrado.calcula_area()}')
