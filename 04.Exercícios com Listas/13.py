
from rich import print
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
for i in range(12):
    while True:
        try:
            temperaturas.append(float(input(f'°C Temperatura Média de {meses[i]}: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma °C Temperatura Válida[/]')
media_anual = sum(temperaturas) / len(temperaturas)
for x in range(12):
    if temperaturas[x] > media_anual:
        print(f'{x + 1} - {meses[x]} Temperatura Média {temperaturas[x]}°C')
