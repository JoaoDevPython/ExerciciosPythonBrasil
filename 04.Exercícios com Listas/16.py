
from rich import print
faixa = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999], [1000, 9999]]
posicao = [0] * 9
while True:
    try:
        comissao = float(input('(0 = Encerrar) Valor Vendido: R$ '))
        soma = 0.09 * comissao + 200
        if comissao == 0:
            break
        for i in range(len(faixa)):
            if faixa[i][0] < soma < faixa[i][1]:
                posicao[i] += 1
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
for x in range(len(faixa)):
    print(f'${faixa[x][0]:4} - ${faixa[x][1]:4}: {posicao[x]}')
