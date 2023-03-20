
from rich import print


def inverter(x):
    return int(str(x)[::-1])


while True:
    try:
        numero = int(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
print(inverter(numero))
