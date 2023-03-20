
import re
from rich import print
contador = 1
while True:
    nome = input('(-1 = Encerrar) Atleta: ').title()
    if nome == '-1':
        break
    elif not re.match(r'^[a-zA-ZÀ-ÿ ]+$', nome):
        print('[red]ERRO. Opção Inválida. Nome deve ser composto apenas por letras[/]')
        continue
    notas = []
    for _ in range(7):
        while True:
            try:
                nota = float(input('Nota: '))
                if nota < 0 or nota > 10:
                    print('[red]ERRO. Nota Inválida. Insira uma Nota de 0 a 10[/]')
                else:
                    notas.append(nota)
                    break
            except KeyboardInterrupt:
                print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
            except ValueError:
                print('[red]ERRO. Insira uma Nota Válida[/]')
    melhor = max(notas)
    pior = min(notas)
    notas.remove(melhor)
    notas.remove(pior)
    media = sum(notas) / len(notas)
    print(f'Resultado Final:\n'
          f'Atleta: {nome}\n'
          f'Melhor Nota: {melhor}\n'
          f'Pior Nota:   {pior}\n'
          f'Média:       {media:.2f}\n')
    contador += 1
