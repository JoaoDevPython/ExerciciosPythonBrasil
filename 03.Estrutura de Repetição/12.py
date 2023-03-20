
from rich import print
while True:
    try:
        numero = int(input('Tabuada de: '))
        if numero < 1 or numero > 10:
            print('[red]ERRO. Tabuada Inválida. Insira um Tabuada de 1 a 10[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
for i in range(1, 11):
    print(f'{numero} x {i:2} = {numero * i}')
