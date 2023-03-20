
from rich import print
while True:
    try:
        numero = int(input('Número: '))
        par_impar = 'Par' if numero % 2 == 0 else 'Ímpar'
        print(par_impar)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
    else:
        break
