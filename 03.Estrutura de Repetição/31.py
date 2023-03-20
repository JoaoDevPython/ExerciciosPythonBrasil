
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print('Lojas Tabajara')
i = 1
precos = []
while True:
    try:
        preco = float(input(f'(0 = Encerrar) Produto {i}: R$ '))
        i += 1
        if preco == 0:
            break
        elif preco < 0:
            print('[red]ERRO. Preço Inválido. Insira um Preço Positivo[/]')
        else:
            precos.append(preco)
            continue
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Preço Válido[/]')
total = sum(precos)
print(f'Total: {locale.currency(total, grouping=True)}')
while True:
    try:
        dinheiro = float(input('Dinheiro: R$ '))
        if dinheiro < total:
            print('[red]ERRO. Valor Insuficiente. Insira um Valor Igual ou Maior que o Total[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
troco = dinheiro - total
print(f'Troco: {locale.currency(troco, grouping=True)}')
