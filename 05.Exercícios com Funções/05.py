
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def soma_imposto(taxa_imposto, custo):
    custo += (custo * (taxa_imposto / 100))
    return locale.currency(custo, grouping=True)


while True:
    try:
        imposto = float(input('Taxa de Imposto (%): '))
        valor = float(input('Custo: R$ '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Taxa ou Custo Válidos[/]')
print(soma_imposto(imposto, valor))
