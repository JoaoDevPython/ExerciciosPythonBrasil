
from rich import print
generos = {'F': 'Feminino', 'M': 'Masculino'}
while True:
    genero = input('Gênero: F ou M: ').upper()
    if genero not in generos:
        print('[red]ERRO. Insira a letra F ou M[/]')
    else:
        break
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
peso_ideal = (62.1 * altura) - 44.7 if genero == 'F' else (72.7 * altura) - 58
print(f'{generos[genero]} | Peso Ideal: {peso_ideal:.3f} kg')
