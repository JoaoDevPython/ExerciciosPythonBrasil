
def desenhar_moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    print('+' + '-' * (colunas - 2) + '+')
    for _ in range(linhas - 2):
        print('|' + ' ' * (colunas - 2) + '|')
    print('+' + '-' * (colunas - 2) + '+')


linha = int(input('Linhas (1 - 20): '))
coluna = int(input('Colunas (1 - 20): '))
desenhar_moldura(linha, coluna)
