
from rich import print
vetor = []
pares = []
impares = []
for i in range(20):
    while True:
        try:
            numero = int(input(f'{i + 1}º Número: '))
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
            vetor.append(numero)
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
        else:
            break
print(f'Vetor:   {", ".join(map(str, vetor))}\n'
      f'Pares:   {", ".join(map(str, pares))}\n'
      f'Ímpares: {", ".join(map(str, impares))}')
