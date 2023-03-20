
from rich import print
while True:
    try:
        numero = float(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/red]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
print(f'O número informado foi {numero}')
