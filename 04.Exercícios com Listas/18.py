
import collections
from rich import print
from rich.console import Console
from rich.table import Table
print('Enquete: Quem foi o melhor jogador?')
contagem = []
while True:
    try:
        voto = int(input('(0 = Encerrar) Número do Jogador: '))
        if voto == 0:
            break
        elif voto < 1 or voto > 23:
            print('[red]ERRO. Informe um Número do Jogador entre 1 e 23 ou 0 para sair[/]')
        else:
            contagem.append(voto)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
print(f'Resultado da Votação:\n'
      f'Foram Computados: {len(contagem)} votos')
tabela = Table(header_style='magenta', border_style='cyan')
tabela.add_column('Jogador')
tabela.add_column('Votos')
tabela.add_column('%', justify='center')
votos = collections.Counter(contagem)
for jogador, votos_jogador in votos.items():
    tabela.add_row(f'{jogador}', f'{votos_jogador}', f'{votos_jogador / len(contagem):.1%}')
console = Console()
console.print(tabela)
mais_votado = max(votos, key=votos.get)
porcentagem = votos[mais_votado] / len(contagem)
print(f'O melhor jogador foi o número {mais_votado}, '
      f'com {votos[mais_votado]} votos, '
      f'correspondendo a {porcentagem:.0%} do total de votos')
