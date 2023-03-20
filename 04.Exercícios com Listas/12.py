
from rich import print
idades = []
alturas = []
for i in range(30):
    while True:
        try:
            idade = int(input(f'{i + 1}º Aluno | Idade: '))
            if idade < 0:
                print('[red]ERRO. Idade Inválida. Insira uma Idade Positiva[/]')
            else:
                idades.append(idade)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Idade Válida[/]')
    while True:
        try:
            altura = float(input(f'{i + 1}º Aluno | Altura em Metros: '))
            if altura < 0:
                print('[red]ERRO. Altura Inválida. Insira uma Altura Positiva[/]')
            else:
                alturas.append(altura)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Altura Válida[/]')
aluno_maior_13 = [alturas[x] for x in range(30) if idades[x] > 13]
media = sum(aluno_maior_13) / len(aluno_maior_13)
media_aluno_maior_13 = [item for item in aluno_maior_13 if item < media]
print(f'Alunos com mais de 13 anos que possuem altura inferior a média: {len(media_aluno_maior_13)}')
