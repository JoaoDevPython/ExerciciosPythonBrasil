
import locale
from rich import print
from rich.console import Console
from rich.table import Table
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        valor_divida = float(input('Valor da Dívida: R$ '))
        if valor_divida < 0:
            print('[red]ERRO. Valor Inválido. Insira um Valor Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Valor da Dívida', style='red')
tabela.add_column('Valor dos Juros', justify='right', style='yellow')
tabela.add_column('Parcelas', justify='right')
tabela.add_column('Valor da Parcela', justify='right', style='green')
for parcelas, juros in [(1, 0), (3, 0.1), (6, 0.15), (9, 0.2), (12, 0.25)]:
    valor_juros = valor_divida * juros
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas
    divida_valor = locale.currency(valor_total, grouping=True)
    juros_valor = locale.currency(valor_juros, grouping=True)
    parcela_valor = locale.currency(valor_parcela, grouping=True)
    tabela.add_row(divida_valor, juros_valor, f'{parcelas}', parcela_valor)
console = Console()
console.print(tabela)
