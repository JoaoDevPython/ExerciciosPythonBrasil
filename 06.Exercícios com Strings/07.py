
import unicodedata
frase = input('Frase: ').upper()
frase_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', frase) if unicodedata.category(c) != 'Mn')
print(f'Espaços em Branco: {frase.count(" ")}\n'
      f'Vogais:\n'
      f'A: {frase_sem_acentos.count("A")}\n'
      f'E: {frase_sem_acentos.count("E")}\n'
      f'I: {frase_sem_acentos.count("I")}\n'
      f'O: {frase_sem_acentos.count("O")}\n'
      f'U: {frase_sem_acentos.count("U")}')
