
from rich import print
while True:
    try:
        valor = float(input('Valor: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
positivo_negativo = 'Positivo' if valor > 0 else 'Negativo' if valor < 0 else 'Nulo'
print(positivo_negativo)
