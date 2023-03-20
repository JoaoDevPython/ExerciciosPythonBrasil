
from rich import print
while True:
    try:
        base = int(input('Base: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Base Válida[/]')
while True:
    try:
        expoente = int(input('Expoente: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Expoente Válido[/]')
resultado = 1
for _ in range(expoente):
    resultado *= base
print(resultado)
