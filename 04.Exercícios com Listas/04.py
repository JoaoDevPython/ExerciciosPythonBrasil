
from rich import print
vetor = []
consoantes = []
for i in range(10):
    while True:
        letras = input(f'{i + 1}ª Letra: ').upper()
        if len(letras) > 1 or not letras.isalpha():
            print('[red]ERRO. Insira uma letra[/]')
            continue
        else:
            if letras not in ('A', 'E', 'I', 'O', 'U'):
                consoantes.append(letras)
            else:
                vetor.append(letras)
        break
print(f'Consoantes lidas: {len(consoantes)}\n'
      f'Consoantes: {", ".join(map(str, consoantes))}')
