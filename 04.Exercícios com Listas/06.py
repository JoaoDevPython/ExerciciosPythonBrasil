
from rich import print
media_aluno = []
for i in range(10):
    notas = []
    for x in range(4):
        while True:
            try:
                nota = float(input(f'Aluno {i + 1} | {x + 1}ª Nota: '))
                if nota < 0 or nota > 10:
                    print('[red]ERRO. Nota Inválida. Insira uma nota de 0 a 10[/]')
                else:
                    notas.append(nota)
                    break
            except KeyboardInterrupt:
                print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
            except ValueError:
                print('[red]ERRO. Insira uma Nota Válida[/]')
    media = sum(notas) / len(notas)
    media_aluno.append(media)
print('Alunos com Média Maior ou Igual a 7.0')
for v in range(10):
    if media_aluno[v] >= 7:
        print(f'{v + 1}º Aluno | Média: {media_aluno[v]}')
