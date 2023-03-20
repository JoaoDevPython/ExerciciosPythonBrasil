
from rich import print
notas = []
for i in range(2):
    while True:
        try:
            nota = float(input(f'{i + 1}ª Nota: '))
            if nota < 0 or nota > 10:
                print('[red]ERRO. Nota Inválida. Insira uma Nota de 0 a 10[/]')
            else:
                notas.append(nota)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Nota Válida[/]')
media = sum(notas) / len(notas)
conceito = 'A' if media >= 9 else 'B' if media >= 7.5 else 'C' if media >= 6 else 'D' if media >= 4 else 'E'
situacao = 'Reprovado' if media < 6 else 'Aprovado'
print(f'Notas: {", ".join(map(str, notas))}'
      f'Média: {media:.2f}\n'
      f'Conceito: {conceito}\n'
      f'Situação: {situacao}')
