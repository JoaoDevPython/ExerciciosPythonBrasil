
from rich import print
while True:
    try:
        numero = int(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
divisores = [i for i in range(1, numero + 1) if numero % i == 0]
if len(divisores) == 2:
    print('Primo')
else:
    print(f'Não é Primo\n'
          f'Divisores: {", ".join(map(str, divisores))}')
