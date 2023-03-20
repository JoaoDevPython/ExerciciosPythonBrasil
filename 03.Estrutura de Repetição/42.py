
from rich import print
from rich.console import Console
from rich.table import Table
intervalos = [0, 0, 0, 0]
while True:
    try:
        numero = int(input('(-1 = Encerrar) Número: '))
        if numero == - 1:
            break
        elif 0 <= numero <= 25:
            intervalos[0] += 1
        elif 25 < numero <= 50:
            intervalos[1] += 1
        elif 50 < numero <= 75:
            intervalos[2] += 1
        elif 75 < numero <= 100:
            intervalos[3] += 1
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
intervalo = Table('0 - 25', '26 - 50', '51 - 75', '76 - 100', header_style='magenta', border_style='cyan')
intervalo.add_row(f'{intervalos[0]}', f'{intervalos[1]}', f'{intervalos[2]}', f'{intervalos[3]}')
console = Console()
console.print(intervalo)
