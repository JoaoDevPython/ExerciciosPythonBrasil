
from rich import print
precos = []
for i in range(3):
    while True:
        try:
            precos.append(float(input(f'{i + 1}º Produto | Preço: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Preço Válido[/]')
indice = precos.index(min(precos)) + 1
print(f'Mais barato: {indice}º Produto')
