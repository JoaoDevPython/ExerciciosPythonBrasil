
from rich import print
while True:
    try:
        nota = float(input('Nota: '))
        if nota < 0 or nota > 10:
            print('[red]ERRO. Nota Inválida. Insira uma Nota de 0 a 10[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Nota Válida[/]')
