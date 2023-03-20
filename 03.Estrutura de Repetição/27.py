
from rich import print
while True:
    try:
        quantidade = int(input('Quantidade de Turmas: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
alunos = []
for i in range(quantidade):
    while True:
        try:
            aluno = int(input(f'{i + 1}ª Turma | Nº Alunos: '))
            if aluno < 0 or aluno > 40:
                print('[red]ERRO. Número de Alunos Inválido. Insira um Número de 0 a 40[/]')
            else:
                alunos.append(aluno)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número de Alunos Válido[/]')
media = sum(alunos) / len(alunos)
print(f'Média de Alunos por Turma: {media} alunos')
