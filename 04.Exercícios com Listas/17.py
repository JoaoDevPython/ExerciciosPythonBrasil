
import re
from rich import print
ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
contador = 1
while True:
    nome = input('(-1 = Encerrar) Atleta: ').title()
    if nome == '-1':
        break
    elif not re.match(r'^[a-zA-ZÀ-ÿ ]+$', nome):
        print('[red]ERRO. Opção Inválida. Nome deve ser composto apenas por letras[/]')
        continue
    saltos = []
    for i in range(5):
        while True:
            try:
                saltos.append(float(input(f'{ordem[i]} Salto: ')))
                break
            except KeyboardInterrupt:
                print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
            except ValueError:
                print('[red]ERRO. Insira um Salto Válido[/]')
    media = sum(saltos) / len(saltos)
    print(f'Resultado Final:\n'
          f'Atleta: {nome}'
          f'Saltos: {" - ".join(map(str, saltos))}'
          f'Média dos Saltos: {media:.1f} m')
    contador += 1
