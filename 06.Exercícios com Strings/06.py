
import re
import datetime
from rich import print
from locale import setlocale, LC_TIME
setlocale(LC_TIME, 'pt_BR')
while True:
    nascimento = input('Data de Nascimento (dd/mm/aaaa): ')
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', nascimento):
        print('[red]ERRO. Opção Inválida. Insira uma data no formato dd/mm/aaaa[/]')
    else:
        break
data = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
data_extenso = data.strftime('%d de %B de %Y')
print(f'Você Nasceu em {data_extenso}')
