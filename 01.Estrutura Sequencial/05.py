
from rich import print
while True:
    try:
        metros = float(input('Tamanho em Metros: '))
        if metros < 0:
            print('[red]ERRO. Tamanho Inválido. Insira um Tamanho Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Tamanho Válido[/]')
centimetros = metros * 100
print(f'{metros} m | convertido | {centimetros} cm')
