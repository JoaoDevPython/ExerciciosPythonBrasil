
from rich import print
while True:
    try:
        numero = int(input('Fatorial: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Fatorial Válido[/]')
print(f'{numero}! = ', end='')
fatorial = 1
for i in range(numero, 0, - 1):
    print(i, end=' . ' if i > 1 else ' = ')
    fatorial *= i
print(fatorial)
