
import random


def embaralhar_palavra(palavra):
    palavra = list(palavra)
    random.shuffle(palavra)
    return ''.join(palavra)


texto = input('Texto: ').upper()
print(embaralhar_palavra(texto))
