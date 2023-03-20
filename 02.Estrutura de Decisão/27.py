
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        morango = float(input('Peso Morangos (kg): '))
        maca = float(input('Peso Maçã (kg): '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Peso Válido[/]')
preco = 0
preco += morango * 2.5 if morango <= 5 else morango * 2.2
preco += maca * 1.8 if maca <= 5 else maca * 1.5
if morango + maca > 8 or preco > 25:
    preco -= preco * 0.1
print(f'Preço Total: {locale.currency(preco, grouping=True)}')
