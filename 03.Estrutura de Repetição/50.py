
from rich import print
while True:
    try:
        n = int(input('Termo: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Termo Válido[/]')
serie = [f'1/{i}' for i in range(1, n + 1)]
series = ' + '.join(serie)
h = sum(1/i for i in range(1, n + 1))
print(f'H = {series}\n'
      f'Valor de H: {h:.2f}')
