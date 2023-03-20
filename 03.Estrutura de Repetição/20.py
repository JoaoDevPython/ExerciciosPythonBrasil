
from rich import print
while True:
    try:
        numero = int(input('Fatorial: '))
        if numero < 0 or numero < 16:
            print('[red]ERRO. Fatorial Inválido. Insira um Fatorial Positivo de 0 a 15[/]')
        else:
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
