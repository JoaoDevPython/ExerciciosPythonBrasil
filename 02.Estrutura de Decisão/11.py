
import locale
from rich import print
from rich.console import Console
from rich.table import Table
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        salario = float(input('Salário: R$ '))
        if salario < 0:
            print('[red]ERRO. Salário Inválido. Insira um Salário Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Salário Válido[/]')
faixas = [(0, 281, 20),
          (281, 701, 15),
          (701, 1501, 10),
          (1501, float('inf'), 5)]
percentual = next((faixa[2] for faixa in faixas if faixa[0] <= salario < faixa[1]), 0)
aumento = salario * (percentual / 100)
novo_salario = salario + aumento
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Descrição')
tabela.add_column('Valor', justify='right')
tabela.add_row('Salário', f'[green]{locale.currency(salario, grouping=True)}[/]')
tabela.add_row('Percentual', f'{percentual}%')
tabela.add_row('Valor do Aumento', f'[green]{locale.currency(aumento, grouping=True)}[/]')
tabela.add_row('Novo Salário', f'[blue]{locale.currency(novo_salario, grouping=True)}[/]')
console = Console()
console.print(tabela)
