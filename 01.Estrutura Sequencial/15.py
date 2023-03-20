
import locale
from rich import print
from rich.console import Console
from rich.table import Table
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
            print('[red]ERRO. Número de Horas Inválido. Insira um Número de Horas Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Descrição')
tabela.add_column('Valor', justify='right')
tabela.add_row('Salário Bruto', f'[green]{locale.currency(salario_bruto, grouping=True)}[/]')
tabela.add_row('IR (11%)', f'[red]{locale.currency(ir, grouping=True)}[/]')
tabela.add_row('INSS (8%)', f'[red]{locale.currency(inss, grouping=True)}[/]')
tabela.add_row('Sindicato (5%)', f'[red]{locale.currency(sindicato, grouping=True)}[/]')
tabela.add_row('Salário Líquido', f'[blue]{locale.currency(salario_liquido, grouping=True)}[/]')
console = Console()
console.print(tabela)
