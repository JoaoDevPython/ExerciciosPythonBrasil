
from rich import print
while True:
    try:
        inicial = int(input('1º Número: '))
        final = int(input('2º Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
for i in range(inicial, final + 1):
    print(i, end=' ')
for i in range(inicial, final - 1, - 1):
    print(i, end=' ')
