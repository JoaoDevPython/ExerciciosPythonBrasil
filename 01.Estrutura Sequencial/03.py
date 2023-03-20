
from rich import print
numeros = []
for i in range(2):
    while True:
        try:
            numeros.append(float(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
soma = sum(numeros)
print(f'Soma: {soma}')
