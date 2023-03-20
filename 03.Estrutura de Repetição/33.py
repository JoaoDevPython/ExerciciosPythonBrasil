
from rich import print
temperaturas = []
while True:
    try:
        graus = input('(X = Encerrar) °C - Temperatura: ').upper()
        if graus == 'X':
            break
        temperaturas.append(float(graus))
        continue
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Temperatura Válida[/]')
menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)
print(f'Menor Temperatura: {menor}°C\n'
      f'Maior Temperatura: {maior}°C\n'
      f'Temperatura Média: {media:.1f}°C')
