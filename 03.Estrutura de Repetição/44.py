
import collections
from rich import print
candidatos = ['José', 'João', 'Ana', 'Bia', 'Nulo', 'Branco']
contagem = []
while True:
    try:
        voto = int(input('(0 = Encerrar) Voto: '))
        if voto == 0:
            break
        elif voto < 1 or voto > 6:
            print('[red]ERRO. Voto Inválido. Insira 1, 2, 3, 4, 5 ou 6[/]')
        else:
            contagem.append(voto)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Voto Válido[/]')
nulo = (contagem.count(4) / len(contagem) * 100)
branco = (contagem.count(5) / len(contagem) * 100)
votos = collections.Counter(contagem)
for candidato, votos_candidato in votos.items():
    print(f'{candidatos[candidato - 1]:6}: {votos_candidato} votos')
print(f'Percentagem Votos Nulos:   {nulo:.2f}%\n'
      f'Percentagem Votos Brancos: {branco:.2f}%')
