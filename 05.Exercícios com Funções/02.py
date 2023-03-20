
from rich import print


def imprimir(n):
    for i in range(1, n + 1):
        print(*range(1, i + 1))


while True:
    try:
        valor = int(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
imprimir(valor)
