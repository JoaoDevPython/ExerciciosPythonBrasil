
from rich import print
while True:
    try:
        celsius = float(input('°C Graus Celsius: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
fahrenheit = celsius * 1.8 + 32
print(f'{celsius:.1f}°C | convertido | {fahrenheit:.1f}°F')
