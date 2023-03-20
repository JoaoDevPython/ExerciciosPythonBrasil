
from rich import print
while True:
    try:
        fahrenheit = float(input('°F Graus Fahrenheit: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
celsius = (fahrenheit - 32) / 1.8
print(f'{fahrenheit:.1f}°F | convertido | {celsius:.1f}°C')
