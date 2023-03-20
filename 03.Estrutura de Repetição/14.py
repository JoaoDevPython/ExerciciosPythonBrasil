
from rich import print
pares = []
impares = []
for i in range(10):
    while True:
        try:
            numero = int(input(f'{i + 1}º Número: '))
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
        else:
            break
print(f'{len(pares)} Pares:     {", ".join(map(str, pares))}\n'
      f'{len(impares)} Ímpares: {", ".join(map(str, impares))}')
