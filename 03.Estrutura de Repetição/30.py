
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print('Panificadora Pão de Ontem - Tabela de Preços')
while True:
    try:
        preco = float(input('Preço do Pão: R$ '))
        if preco < 0:
            print('[red]ERRO. Preço Inválido. Insira um Preço Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Preço Válido[/]')
for i in range(1, 51):
    preco_total = i * preco
    print(f'{i:2} - {locale.currency(preco_total, grouping=True)}')
