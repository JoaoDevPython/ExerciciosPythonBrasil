
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        valor_hora = float(input('Valor Hora: R$ '))
        if valor_hora < 0:
            print('[red]ERRO. Valor Inválido. Insira um Valor Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
while True:
    try:
        horas_trabalhadas = int(input('Número de Horas Trabalhadas: '))
        if horas_trabalhadas < 0:
            print('[red]ERRO. Valor Inválido. Insira um Número de Horas Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
salario = valor_hora * horas_trabalhadas
print(f'Salário Mensal: {locale.currency(salario, grouping=True)}')
