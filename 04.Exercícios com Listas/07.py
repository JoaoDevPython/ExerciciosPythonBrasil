
from rich import print
vetor = []
for i in range(5):
    while True:
        try:
            vetor.append(int(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
soma = sum(vetor)
multiplicacao = 1
for x in vetor:
    multiplicacao *= x
print(f'Números: {", ".join(map(str, vetor))}'
      f'Soma: {soma}\n'
      f'Multiplicação: {multiplicacao}')
