
from rich import print
while True:
    try:
        termo = int(input('Termo: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Termo Válido[/]')
fibonacci = [1, 1]
fibonacci.extend(fibonacci[i - 1] + fibonacci[i - 2] for i in range(2, termo))
print(fibonacci[- 1])
