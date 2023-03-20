
import re
from rich import print
print('Valida e Corrige Número de Telefone')
while True:
    telefone = input('Telefone: ')
    telefone = telefone.replace('-', '')
    if not telefone.isdigit():
        print('[red]ERRO. Telefone Inválido. Telefone deve conter apenas números')
        continue
    elif len(telefone) == 7:
        telefone = f'3{telefone}'
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente')
    telefone = re.sub(r'(\d{4})(\d{4})', r'\1-\2', telefone)
    print(f'Telefone corrigido sem formatação: {telefone.replace("-", "")}\n'
          f'Telefone corrigido com formatação: {telefone}')
    break
