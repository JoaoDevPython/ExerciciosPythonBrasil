
from rich import print


def informar_quantidade(x):
    return len(str(x))


while True:
    try:
        valor = int(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
print(f'{informar_quantidade(valor)} dígitos')
