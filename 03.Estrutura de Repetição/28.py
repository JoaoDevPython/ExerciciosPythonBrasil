
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        quantidade = int(input('Quantidade de CDs: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
precos = []
for i in range(quantidade):
    while True:
        try:
            preco = float(input(f'{i + 1}º CD: R$ '))
            if preco < 0:
                print('[red]ERRO. Preço Inválido. Insira um Preço Positivo[/]')
            else:
                precos.append(preco)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Preço Válido[/]')
total = sum(precos)
media = sum(precos) / len(precos)
print(f'Valor Total: {locale.currency(total, grouping=True)}\n'
      f'Valor Médio: {locale.currency(media, grouping=True)}')
