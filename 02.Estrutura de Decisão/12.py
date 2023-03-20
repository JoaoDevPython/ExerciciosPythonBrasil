
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
            print('[red]ERRO. Valor Inválido. Insira um Número de Horas Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número de Horas Válido[/]')
salario_bruto = valor_hora * horas_trabalhadas
faixas = [(0, 901, 0),
          (901, 1501, 5),
          (1501, 2501, 10),
          (2501, float('inf'), 20)]
desconto_ir = next((faixa[2] for faixa in faixas if faixa[0] <= salario_bruto < faixa[1]), 0)
ir = salario_bruto * (desconto_ir / 100)
inss = salario_bruto * 0.1
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Descrição')
tabela.add_column('Valor', justify='right')
tabela.add_row('Salário Bruto', f'[green]{locale.currency(salario_bruto, grouping=True)}[/]')
tabela.add_row(f'IR ({desconto_ir}%)', f'[red]{locale.currency(ir, grouping=True)}[/]')
tabela.add_row('INSS (10%)', f'[red]{locale.currency(inss, grouping=True)}[/]')
tabela.add_row('Sindicato (3%)', f'[red]{locale.currency(sindicato, grouping=True)}[/]')
tabela.add_row('FGTS (11%)', locale.currency(fgts, grouping=True))
tabela.add_row('Total de Descontos', f'[red]{locale.currency(descontos, grouping=True)}[/]')
tabela.add_row('Salário Líquido', f'[blue]{locale.currency(salario_liquido, grouping=True)}[/]')
console = Console()
console.print(tabela)
