
from rich import print
from rich.panel import Panel


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'{self.x} {self.y}')


class Retangulo:
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto

    def centro(self):
        x_centro = self.ponto.x + self.largura / 2
        y_centro = self.ponto.y + self.altura / 2
        return Ponto(x_centro, y_centro)

    def imprimir_centro(self):
        centro = self.centro()
        print('Centro do Retângulo:')
        centro.imprimir()


retangulo1 = Retangulo(5, 10, Ponto(0, 0))
retangulo2 = Retangulo(3, 6, Ponto(2, 3))
print('Vértices de Partida:\n'
      'Retângulo 1:')
retangulo1.ponto.imprimir()
print('Retângulo 2:')
retangulo2.ponto.imprimir()
retangulo1.imprimir_centro()
retangulo2.imprimir_centro()
while True:
    print(Panel('1 - Alterar Largura do Retângulo 1\n'
                '2 - Alterar Altura do Retângulo 1\n'
                '3 - Alterar Ponto de Partida do Retângulo 1\n'
                '4 - Imprimir Centro do Retângulo 1\n'
                '5 - Alterar Largura do Retângulo 2\n'
                '6 - Alterar Altura do Retângulo 2\n'
                '7 - Alterar Ponto de Partida do Retângulo 2\n'
                '8 - Imprimir Centro do Retângulo 2\n'
                '0 - Sair',
                title='Menu', border_style='cyan', expand=False))
    opcao = int(input('Escolha uma Opção: '))
    if opcao == 1:
        largura2 = float(input('Nova Largura: '))
        retangulo1.largura = largura2
    elif opcao == 2:
        altura2 = float(input('Nova Altura: '))
        retangulo1.altura = altura2
    elif opcao == 3:
        x2 = float(input('Novo Valor de X: '))
        y2 = float(input('Novo Valor de Y: '))
        retangulo1.ponto = Ponto(x2, y2)
    elif opcao == 4:
        retangulo1.imprimir_centro()
    elif opcao == 5:
        largura2 = float(input('Nova Largura: '))
        retangulo2.largura = largura2
    elif opcao == 6:
        altura2 = float(input('Nova Altura: '))
        retangulo2.altura = altura2
    elif opcao == 7:
        x2 = float(input('Novo Valor de X: '))
        y2 = float(input('Novo Valor de Y: '))
        retangulo2.ponto = Ponto(x2, y2)
    elif opcao == 8:
        retangulo2.imprimir_centro()
    elif opcao == 0:
        break
    else:
        print('Opção Inválida')
