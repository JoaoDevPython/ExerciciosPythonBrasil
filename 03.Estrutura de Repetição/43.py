
import collections
import locale
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
menu = {100: ['Cachorro Quente', 1.2],
        101: ['Bauru Simples', 1.3],
        102: ['Bauru com Ovo', 1.5],
        103: ['Hambúrguer', 1.2],
        104: ['Cheeseburguer', 1.3],
        105: ['Refrigerante', 1.]}
total_compra = 0
compras = collections.defaultdict(int)
while True:
    print(Panel('100: Cachorro Quente\n'
                '101: Bauru Simples\n'
                '102: Bauru com Ovo\n'
                '103: Hambúrguer\n'
                '104: Cheeseburguer\n'
                '105: Refrigerante',
                title='Menu', border_style='cyan', expand=False))
    try:
        codigo = int(input('(0 = Encerrar) Código do Produto: '))
        if codigo == 0:
            break
        elif codigo not in menu:
            print(':rage:[red]ERRO. Código Inválido.[/]')
            continue
        else:
            while True:
                try:
                    quantidade = int(input('Quantidade Desejada: '))
                    if quantidade < 0:
                        print('[red]ERRO. Quantidade Inválida. Insira uma Quantidade Positiva[/]')
                    else:
                        break
                except KeyboardInterrupt:
                    print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
                except ValueError:
                    print('[red]ERRO. Insira uma Quantidade Válida[/]')
        valor_item = quantidade * menu[codigo][1]
        total_compra += valor_item
        compras[codigo] += quantidade
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Código Válido[/]')
        continue
cardapio = Table(header_style='magenta', border_style='cyan')
cardapio.add_column('Especificação')
cardapio.add_column('Valor Unitário', justify='right', style='green')
cardapio.add_column('Quantidade', justify='right')
cardapio.add_column('Valor Total', justify='right', style='green')
for codigo, quantidade in compras.items():
    descricao = menu[codigo][0]
    preco_unitario = locale.currency(menu[codigo][1], grouping=True)
    preco_total = locale.currency(quantidade * menu[codigo][1], grouping=True)
    cardapio.add_row(descricao, preco_unitario, f'{quantidade}', preco_total)
soma_preco_total = locale.currency(total_compra, grouping=True)
cardapio.add_row('', '', '', f'[blue]{soma_preco_total}[/]')
console = Console()
console.print(cardapio)
