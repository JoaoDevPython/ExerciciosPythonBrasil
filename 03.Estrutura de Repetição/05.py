
from rich import print
while True:
    while True:
        try:
            pais_a = int(input('População País A: '))
            pais_b = int(input('População País B: '))
            if pais_b < pais_a:
                print('[red]ERRO. População B deve ser maior que a de A[/]')
            elif pais_a < 0 or pais_b < 0:
                print('[red]ERRO. População Inválida. Insira uma População Positiva[/]')
            else:
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. População Inválida. Insira uma População Válida[/]')
    while True:
        try:
            taxa_a = float(input('Crescimento País A: '))
            taxa_b = float(input('Crescimento País B: '))
            if taxa_b > taxa_a:
                print('[red]ERRO. Taxa B deve ser menor que a de A[/]')
            elif taxa_a < 0 or taxa_b < 0:
                print('[red]ERRO. Taxa Inválida. Insira uma Taxa Positiva[/]')
            else:
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Taxa Inválida. Insira uma Taxa Válida[/]')
    anos = 0
    while pais_a < pais_b:
        pais_a *= 1 + (taxa_a / 100)
        pais_b *= 1 + (taxa_b / 100)
        anos += 1
    print(f'Ultrapassa em {anos} anos')
    if input('Deseja Continuar? S ou N: ').upper() != 'S':
        break
