
from rich import print
while True:
    try:
        quantidade = int(input('Quantidade de Notas: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
notas = []
for i in range(quantidade):
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
            print('[red]ERRO. Insira um Nota Válida[/]')
media = sum(notas) / len(notas)
print(f'Média: {media:.2f}')
