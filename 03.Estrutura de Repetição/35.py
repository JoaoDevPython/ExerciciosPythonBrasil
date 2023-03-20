
from rich import print
while True:
    try:
        numero = int(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
primos = []
for i in range(2, numero):
    divisores = [x for x in range(1, numero + 1) if i % x == 0]
    if len(divisores) == 2:
        divisores.sort(reverse=True)
        primos.append(divisores[0])
print(f'Primos entre 1 e {numero}: {", ".join(map(str, primos))}')
