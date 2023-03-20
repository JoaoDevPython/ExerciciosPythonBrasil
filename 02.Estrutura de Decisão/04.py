
from rich import print
while True:
    letra = input('Letra: ').upper()
    if len(letra) > 1 or not letra.isalpha():
        print('[red]ERRO. Insira apenas uma letra[/]')
        continue
    else:
        if letra not in ('A', 'E', 'I', 'O', 'U'):
            print('Consoante')
        else:
            print('Vogal')
    break
