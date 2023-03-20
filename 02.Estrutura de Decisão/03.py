
from rich import print
generos = {'F': 'Feminino', 'M': 'Masculino'}
while True:
    letra = input('Gênero: F ou M: ').upper()
    if letra not in generos:
        print('[red]ERRO. Sexo Inválido. Insira a letra F ou M[/]')
    else:
        break
print(generos[letra])
