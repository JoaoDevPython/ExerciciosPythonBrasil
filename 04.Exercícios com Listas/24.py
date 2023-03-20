
import random
aleatorios = []
for _ in range(100):
    dado = random.randint(1, 6)
    aleatorios.append(dado)
for i in range(1, 7):
    print(f'Valor: {i} | Gerado: {aleatorios.count(i)} Vezes')
