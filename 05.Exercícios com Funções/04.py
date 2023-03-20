
from rich import print


def positivo_negativo(x):
    return 'P' if x > 0 else 'N'


while True:
    try:
        valor = float(input('Valor: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
print(positivo_negativo(valor))
