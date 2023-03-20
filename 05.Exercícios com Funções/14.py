
import itertools


def quadrado_magico(quadrado):
    soma = sum(quadrado[0])
    for i in range(3):
        if sum(quadrado[1]) != soma:
            return False
        coluna_i = [quadrado[x][i] for x in range(3)]
        if sum(coluna_i) != soma:
            return False
    diagonal1 = [quadrado[i][i] for i in range(3)]
    if sum(diagonal1) != soma:
        return False
    diagonal2 = [quadrado[i][2 - i] for i in range(3)]
    return sum(diagonal2) == soma


permutacoes = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))
for permutacao in permutacoes:
    matriz = [permutacao[i:i + 3] for i in range(0, 9, 3)]
    if quadrado_magico(matriz):
        print(' '.join(str(x) for x in matriz[0]))
        print(' '.join(str(x) for x in matriz[1]))
        print(' '.join(str(x) for x in matriz[2]))
        print()
