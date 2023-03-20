
from math import ceil, floor
import locale
from rich import print, box
from rich.panel import Panel
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        area = float(input('Tamanho em Metros (m²): '))
        if area < 0:
            print('[red]ERRO. Tamanho Inválido. Insira um Tamanho Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Tamanho Válido[/]')
tinta_necessaria = ceil((area / 6) * 1.1)
latas = ceil(tinta_necessaria / 18)
preco_latas = latas * 80
galoes = ceil(tinta_necessaria / 3.6)
preco_galoes = galoes * 25
mix_latas = floor(tinta_necessaria / 18)
mix_galoes = ceil((tinta_necessaria % 18) / 3.6)
preco_mix = mix_latas * 80 + mix_galoes * 25
print(Panel(f'Quantidade:  {latas}\n'
            f'Preço Total: {locale.currency(preco_latas, grouping=True)}',
            title='Latas de 18L', box=box.DOUBLE, border_style='green', expand=False))
print(Panel(f'Quantidade:  {galoes}\n'
            f'Preço Total: {locale.currency(preco_galoes, grouping=True)}',
            title='Galões de 3,6L', box=box.DOUBLE, border_style='yellow', expand=False))
print(Panel(f'Latas de 18L:   {mix_latas}\n'
            f'Galões de 3,6L: {mix_galoes}\n'
            f'Preço Total: {locale.currency(preco_mix, grouping=True)}',
            title='Mix de Tintas', box=box.DOUBLE, border_style='blue', expand=False))
