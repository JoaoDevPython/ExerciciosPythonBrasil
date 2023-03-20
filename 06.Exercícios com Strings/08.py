
import unicodedata
frase = input('Frase: ').upper()
frase_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', frase) if unicodedata.category(c) != 'Mn')
frase_sem_espacos = frase_sem_acentos.replace(' ', '').replace('-', '').replace('.', '').replace(',', '')
frase_invertida = frase_sem_espacos[::-1]
resultado = 'Palíndromo' if frase_sem_espacos == frase_invertida else 'Não é Palíndromo'
print(resultado)
