
from rich import print
from rich.console import Console
from rich.table import Table
defeitos = [0, 0, 0, 0]
tipos_defeitos = ['Necessita da Esfera',
                  'Necessita de Limpeza',
                  'Necessita Troca do Cabo ou Conector',
                  'Quebrado ou Inutilizado']
while True:
    try:
        tipo_defeito = int(input('(0 = Encerrar) Tipo de Defeito: '))
        if tipo_defeito == 0:
            break
        elif tipo_defeito < 1 or tipo_defeito > 4:
            print('[red]ERRO. Tipo Inválido. Insira um Tipo de 1 a 4[/]')
            continue
        defeitos[tipo_defeito - 1] += 1
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Tipo Válido[/]')
print(f'Quantidade de Mouses: {sum(defeitos)}')
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Situação')
tabela.add_column('Quantidade', justify='right')
tabela.add_column('Percentual', justify='right')
for i, quantidade in enumerate(defeitos):
    tabela.add_row(f'{i + 1} - {tipos_defeitos[i]}', f'{quantidade}', f'{quantidade / sum(defeitos) * 100:.0f}%')
console = Console()
console.print(tabela)
