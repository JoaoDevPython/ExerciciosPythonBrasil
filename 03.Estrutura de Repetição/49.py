
from rich import print
while True:
    try:
        n = int(input('Termo: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Termo Válido[/]')
serie = []
soma = 0
for i in range(1, n + 1):
    termo = f'{i}/{2 * i - 1}'
    serie.append(termo)
    soma += i / (2 * i - 1)
print(f'S = {" + ".join(serie)}\n'
      f'Soma: {soma:.2f}')
