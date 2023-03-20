
from rich import print
vetor1 = []
for i in range(10):
    while True:
        try:
            vetor1.append(int(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
vetor2 = []
for x in range(10):
    while True:
        try:
            vetor2.append(int(input(f'{x + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
vetor3 = []
for v in range(10):
    vetor3.extend((vetor1[v], vetor2[v]))
print(f'{", ".join(map(str, vetor3))}')
