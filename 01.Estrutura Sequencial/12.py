
from rich import print
while True:
    try:
        altura = float(input('Altura em Metros: '))
        if altura < 0:
            print('[red]ERRO. Altura Inválida. Insira uma Altura Positiva[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Altura Válida[/]')
peso_ideal = (72.7 * altura) - 58
print(f'Peso Ideal: {peso_ideal:.3f} kg')
