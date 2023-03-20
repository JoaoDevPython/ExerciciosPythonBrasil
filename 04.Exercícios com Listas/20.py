
import locale
from rich import print
from rich.console import Console
from rich.table import Table
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
salarios = []
while True:
    try:
        salario = float(input('(0 = Encerrar) Salário: R$ '))
        if salario == 0:
            break
        elif salario < 0:
            print('[red]ERRO. Salário Inválido. Insira um Salário Positivo[/]')
            continue
        abono = 0
        abono = 100 if salario < 500 else salario * 0.2
        salarios.append((salario, abono))
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Salário Válido[/]')
total_abonos = sum(abono for _, abono in salarios)
minimo = sum(abono == 100 for _, abono in salarios)
maior_abono = max(abono for _, abono in salarios)
tabela = Table(title='Projeção de Gastos com Abono', header_style='magenta', border_style='cyan')
tabela.add_column('Salário', justify='right')
tabela.add_column('Abono', justify='right')
for salario, abono in salarios:
    tabela.add_row(locale.currency(salario, grouping=True), locale.currency(abono, grouping=True))
console = Console()
console.print(tabela)
print(f'Foram Processados {len(salarios)} Colaboradores\n'
      f'Total Gasto com Abonos: {locale.currency(total_abonos, grouping=True)}\n'
      f'Valor Mínimo Pago a {minimo} Colaboradores\n'
      f'Maior Valor de Abono Pago: {locale.currency(maior_abono, grouping=True)}')
