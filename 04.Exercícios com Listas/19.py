
import collections
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
contagem = []
while True:
    print(Panel('As possíveis respostas são:\n'
                '1 - Windows Server\n'
                '2 - Unix\n'
                '3 - Linux\n'
                '4 - Netware\n'
                '5 - Mac OS\n'
                '6 - Outro',
                title='Qual o melhor Sistema Operacional para uso de servidores?',
                border_style='cyan', expand=False))
    try:
        voto = int(input('(0 = Encerrar) Sistema Operacional: '))
        if voto == 0:
            break
        elif voto < 1 or voto > 6:
            print('[red]ERRO. Informe uma Opção entre 1 e 6 ou 0 para sair[/]')
        else:
            contagem.append(voto)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Sistema Operacional')
tabela.add_column('Votos')
tabela.add_column('%', justify='center')
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos = collections.Counter(contagem)
for s_o, votos_s_o in votos.items():
    tabela.add_row(sistemas[s_o - 1], f'{votos_s_o}', f'{votos_s_o / len(contagem):.0%}')
tabela.add_row('Total', f'{len(contagem)}', '')
console = Console()
console.print(tabela)
mais_votado = max(votos, key=votos.get)
porcentagem = votos[mais_votado] / len(contagem)
print(f'O Sistema Operacional mais votado foi o {sistemas[mais_votado - 1]}, '
      f'com {votos[mais_votado]} votos, '
      f'correspondendo a {porcentagem:.0%} do total de votos')
