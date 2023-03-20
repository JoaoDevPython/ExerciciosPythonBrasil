
from rich import print
while True:
    try:
        lado = float(input('Comprimento do Lado: '))
        if lado < 0:
            print('[red]ERRO. Comprimento Inválido. Insira um Comprimento Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Comprimento Válido[/]')
area = lado ** 2
dobro = area * 2
print(f'Área:  {area:.2f} m²\n'
      f'Dobro: {dobro:.2f} m²')
