
from rich import print
vetor = []
for i in range(10):
    while True:
        try:
            numero = int(input(f'{i + 1}º Número: '))
            quadrados = numero ** 2
            vetor.append(quadrados)
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
soma = sum(vetor)
print(f'Soma dos Quadrados: {soma}')
