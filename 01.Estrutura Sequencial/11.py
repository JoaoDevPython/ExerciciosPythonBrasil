
from rich import print
numeros = []
for i in range(3):
    while True:
        try:
            if i < 2:
                numeros.append(int(input(f'{i + 1}º Número Inteiro: ')))
            else:
                numeros.append(float(input(f'{i - 1}º Número Real: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
resposta1 = (numeros[0] * 2) * (numeros[1] / 2)
resposta2 = numeros[0] * 3 + numeros[2]
resposta3 = numeros[2] ** 3
print(f'A: {resposta1:.0f}\n'
      f'B: {resposta2}\n'
      f'C: {resposta3:.2f}')
