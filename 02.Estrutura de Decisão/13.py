
from rich import print
dias = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
while True:
    try:
        numero = int(input('Número: '))
        if numero not in dias:
            print('[red]ERRO. Insira um Número de 1 a 7[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
print(dias[numero])
