
frase1 = input('String 1: ')
frase2 = input('String 2: ')
if len(frase1) == len(frase2):
    tamanho = 'As duas strings são de tamanhos iguais'
else:
    tamanho = 'As duas strings são de tamanhos diferentes'
if frase1 == frase2:
    conteudo = 'As duas strings possuem conteúdo igual'
else:
    conteudo = 'As duas strings possuem conteúdo diferente'
print(f'Compara Duas Strings\n'
      f'String 1: {frase1}\n'
      f'String 2: {frase2}\n'
      f'Tamanho de "{frase1}": {len(frase1)} caracteres\n'
      f'Tamanho de "{frase2}": {len(frase2)} caracteres\n'
      f'{tamanho}\n'
      f'{conteudo}')
