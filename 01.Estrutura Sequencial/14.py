
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        peso = float(input('Peso (kg): '))
        if peso < 0:
            print('[red]ERRO. Peso Inválido. Insira um Peso Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Peso Válido[/]')
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Excesso: {excesso:.3f} kg\n'
          f'Multa: {locale.currency(multa, grouping=True)}')
else:
    print('Não há Excesso')
