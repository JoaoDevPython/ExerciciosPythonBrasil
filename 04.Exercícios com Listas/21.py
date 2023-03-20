
import locale
from rich import print
from rich.console import Console
from rich.table import Table
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print('Comparativo de Consumo de Combustível')
modelos = []
consumos = []
preco_gasolina = 2.25
for i in range(5):
    modelos.append(input(f'Veículo {i + 1} | Nome: '))
    while True:
        try:
            consumo = float(input('km por Litro: '))
            if consumo < 0:
                print('[red]ERRO. Valor Inválido. Insira um Valor Positivo[/]')
            else:
                consumos.append(consumo)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Valor Válido[/]')
tabela = Table(title='Relatório Final', header_style='magenta', border_style='cyan', show_header=False)
for i, modelo in enumerate(modelos):
    litros = 1000 / consumos[i]
    precos = litros * preco_gasolina
    custo = locale.currency(precos, grouping=True)
    tabela.add_row(f'{i + 1}', f'{modelo}', f'{consumos[i]:4}', f'{litros:5.1f} litros', f'{custo}')
console = Console()
console.print(tabela)
indice_menor_consumo = consumos.index(max(consumos))
print(f'O Menor Consumo é do {modelos[indice_menor_consumo]}')
