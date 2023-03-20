
from math import pi
from rich import print
while True:
    try:
        raio = float(input('Raio do Círculo: '))
        if raio < 0:
            print('[red]ERRO. Raio Inválido. Insira um Raio Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Raio Válido[/]')
area = pi * raio ** 2
print(f'Área: {area:.2f} m²')
