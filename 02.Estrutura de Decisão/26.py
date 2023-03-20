
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
combustiveis = {'A': 'Álcool', 'G': 'Gasolina'}
while True:
    opcao = input('Combustíveis: A - Álcool ou G - Gasolina: ').upper()
    if opcao not in combustiveis:
        print('[red]ERRO. Insira um Combustível: A ou G[/]')
    else:
        break
while True:
    try:
        litros = float(input('Quantidade em Litros: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
preco = 0
if opcao == 'A':
    preco = litros * 1.9
    preco -= litros * 1.9 * 0.03 if litros <= 20 else litros * 1.9 * 0.05
elif opcao == 'G':
    preco = litros * 2.5
    preco -= litros * 2.5 * 0.04 if litros <= 20 else litros * 2.5 * 0.06
print(f'{combustiveis[opcao]} | {litros} L\n'
      f'Preço Total: {locale.currency(preco, grouping=True)}')
