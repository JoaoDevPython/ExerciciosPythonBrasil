
import random
from rich import print
from rich.panel import Panel


class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)
        self.saude = random.randint(0, 10)

    def __str__(self):
        return (f'Bichinho: {self.nome}\n'
                f'Fome: {self.fome}\n'
                f'Tédio: {self.tedio}\n'
                f'Saúde: {self.saude}')

    def alimentar(self, quantidade):
        self.fome = max(self.fome - quantidade, 0)

    def brincar(self, minutos):
        self.tedio = max(self.tedio - minutos, 0)

    def ouvir(self):
        self.saude = min(self.saude + 1, 10)
        self.tedio = max(self.tedio - 1, 0)


class FazendaBichinhos:
    def __init__(self, nomes):
        self.bichinhos = [BichinhoVirtual(nome) for nome in nomes]

    def executar_opcao(self, opcoes):
        if opcoes == 1:
            quantidade = int(input('Quantidade de Comida: '))
            for bichinho in self.bichinhos:
                bichinho.alimentar(quantidade)

        elif opcoes == 2:
            minutos = int(input('Minutos de Brincadeira: '))
            for bichinho in self.bichinhos:
                bichinho.brincar(minutos)

        elif opcoes == 3:
            for bichinho in self.bichinhos:
                bichinho.ouvir()

        elif opcoes == 4:
            for bichinho in self.bichinhos:
                print(bichinho)

        else:
            print('Opção Inválida')


if __name__ == '__main__':
    nomes_bichinhos = ['Buddy', 'Lucky', 'Fluffy', 'Fido', 'Rex']
    fazenda = FazendaBichinhos(nomes_bichinhos)
    while True:
        print(Panel('1 - Alimentar todos os bichinhos\n'
                    '2 - Brincar com todos os bichinhos\n'
                    '3 - Ouvir todos os bichinhos\n'
                    '4 - Mostrar todos os bichinhos\n'
                    '0 - Sair',
                    title='Menu', border_style='cyan', expand=False))
        opcao = int(input('Escolha uma Opção: '))
        if opcao == 0:
            break
        fazenda.executar_opcao(opcao)
