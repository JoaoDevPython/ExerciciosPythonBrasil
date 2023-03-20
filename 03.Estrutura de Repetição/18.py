
from rich import print
while True:
    try:
        quantidade = int(input('Quantidade de Números: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
numeros = []
for i in range(quantidade):
    while True:
        try:
            numeros.append(float(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)
print(f'Menor: {menor}\n'
      f'Maior: {maior}\n'
      f'Soma:  {soma}')
