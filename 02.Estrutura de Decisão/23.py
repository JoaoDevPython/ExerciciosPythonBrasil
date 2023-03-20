
from rich import print
while True:
    try:
        numero = float(input('Número: '))
        inteiro_decimal = 'Inteiro' if numero == round(numero) else 'Decimal'
        print(inteiro_decimal)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
    else:
        break
