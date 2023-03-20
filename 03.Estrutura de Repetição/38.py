
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        salario = float(input('Salário Inicial: R$ '))
        if salario < 0:
            print('[red]ERRO. Salário Inválido. Insira um Salário Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Salário Válido[/]')
aumento = 1.5
for _ in range(1996, 2024):
    salario += salario * aumento / 100
    aumento *= 2
print(f'Salário Atual: {locale.currency(salario, grouping=True)}')
