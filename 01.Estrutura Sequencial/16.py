
from math import ceil
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        area = float(input('Tamanho em Metros (m²): '))
        if area < 0:
            print('[red]ERRO. Tamanho Inválido. Insira um Tamanho Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Tamanho Válido[/]')
tinta_necessaria = ceil(area / 3)
latas = ceil(tinta_necessaria / 18)
preco = latas * 80
print(f'Quantidade de latas 18L: {latas}\n'
      f'Preço Total: {locale.currency(preco, grouping=True)}')
