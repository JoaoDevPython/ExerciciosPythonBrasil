
import time
from rich import print
from rich.panel import Panel


class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.fome = 0
        self.saude = 100
        self.tedio = 0

    def alimentar(self, quantidade):
        self.fome -= quantidade / 2
        self.fome = max(self.fome, 0)
        print(f'Você alimentou o {self.nome} com {quantidade} de comida')
        self.mostrar_status()

    def brincar(self, tempo):
        self.tedio -= tempo / 2
        self.tedio = max(self.tedio, 0)
        print(f'Você brincou com {self.nome} por {tempo} minutos')
        self.mostrar_status()

    def envelhecer(self):
        self.idade += 1
        self.fome += 5
        self.saude -= 5
        self.tedio += 5
        self.mostrar_status()

    def mostrar_status(self):
        print(f'Nome:  {self.nome}\n'
              f'Idade: {self.idade}\n'
              f'Fome:  {self.fome}\n'
              f'Saúde: {self.saude}\n'
              f'Tédio: {self.tedio}')


rex = BichinhoVirtual('Rex')
while True:
    print(Panel('1 - Alimentar o bichinho\n'
                '2 - Brincar com o bichinho\n'
                '3 - Envelhecer o bichinho\n'
                '0 - Sair do Programa',
                title='Menu', border_style='cyan', expand=False))

    escolha = int(input('Escolha uma Opção: '))
    if escolha == 1:
        quantidade_x = int(input('Quanto de comida você quer dar ao bichinho?: '))
        rex.alimentar(quantidade_x)
    elif escolha == 2:
        tempo_x = int(input('Por quanto tempo você quer brincar com o bichinho (minutos)?: '))
        rex.brincar(tempo_x)
    elif escolha == 3:
        rex.envelhecer()
    elif escolha == 0:
        break
    else:
        print('Opção Inválida')
taxa_fome = 5 + rex.idade // 10
taxa_tedio = 5 + rex.idade // 10
rex.fome += taxa_fome
rex.tedio += taxa_tedio
rex.mostrar_status()
time.sleep(1)
