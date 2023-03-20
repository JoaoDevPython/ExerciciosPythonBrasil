
from rich import print
while True:
    try:
        numero = int(input('Número: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
contador = sum(numero % i == 0 for i in range(1, numero + 1))
primo_nao_primo = 'Primo' if contador == 2 else 'Não é Primo'
print(primo_nao_primo)
