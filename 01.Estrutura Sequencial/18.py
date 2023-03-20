
from rich import print
while True:
    try:
        tamanho = int(input('Tamanho do Arquivo (MB): '))
        if tamanho < 0:
            print('[red]ERRO. Tamanho Inválido. Insira um Tamanho Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Tamanho Válido[/]')
while True:
    try:
        velocidade = int(input('Velocidade de Internet (Mbit/s): '))
        if velocidade < 0:
            print('[red]ERRO. Velocidade Inválida. Insira uma Velocidade Positiva[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Velocidade Válida[/]')
tempo = tamanho / (velocidade / 8)
horas, resto = divmod(tempo, 3600)
minutos, segundos = divmod(resto, 60)
print(f'Tempo de Download: {int(horas)} horas {int(minutos)} minutos {int(segundos)} segundos')
