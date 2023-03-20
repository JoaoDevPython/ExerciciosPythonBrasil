
from rich import print
while True:
    try:
        numero = int(input('Tabuada de: '))
        if numero < 1 or numero > 10:
            print('[red]ERRO. Tabuada Inválida. Insira um Tabuada de 1 a 10[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Tabuada Válida[/]')
while True:
    try:
        inicial = int(input('Começar por: '))
        final = int(input('Terminar em: '))
        if final < inicial:
            print('[red]ERRO. Final deve ser maior que o Inicial[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
print(f'Vou montar a tabuada de {numero} começando em {inicial} e terminando em {final}')
for i in range(inicial, final + 1):
    print(f'{numero} x {i} = {numero * i}')
