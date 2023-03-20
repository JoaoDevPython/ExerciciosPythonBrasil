
import collections
from rich import print
while True:
    try:
        quantidade = int(input('Quantidade de Eleitores: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
candidatos = ['Ana', 'Bia', 'Lea']
contagem = []
for _ in range(quantidade):
    while True:
        try:
            voto = int(input('Voto: '))
            if voto < 1 or voto > 3:
                print('[red]ERRO. Voto Inválido. Insira um 1, 2 ou 3[/]')
            else:
                contagem.append(voto)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Voto Válido[/]')
votos = collections.Counter(contagem)
for candidato, votos_candidato in votos.items():
    print(f'{candidatos[candidato - 1]}: {votos_candidato} votos')
