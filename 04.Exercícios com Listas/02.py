
from rich import print
vetor = []
for i in range(10):
    while True:
        try:
            vetor.append(float(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
vetor.reverse()
print(f'Ordem Inversa: {", ".join(map(str, vetor))}')
