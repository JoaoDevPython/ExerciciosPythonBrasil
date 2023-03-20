
import re
from rich import print
while True:
    nome = input('Nome: ').upper()
    if not re.match(r'^[a-zA-ZÀ-ÿ ]+$', nome):
        print('[red]ERRO. Opção Inválida. Nome deve ser composto apenas por letras[/]')
    else:
        break
for letra in nome:
    print(letra)
