
from rich import print
numeros = []
for i in range(5):
    while True:
        try:
            numeros.append(float(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
soma = sum(numeros)
media = sum(numeros) / len(numeros)
print(f'Soma: {soma}\n'
      f'Média: {media:.2f}')
