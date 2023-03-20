
import datetime
from rich import print
datas = input('Data: dd/mm/aaaa: ')
try:
    data = datetime.datetime.strptime(datas, '%d/%m/%Y')
    situacao = 'Data Futura' if data > datetime.datetime.now() else 'Data Válida'
    print(situacao)
except KeyboardInterrupt:
    print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
except ValueError:
    print('Data Inválida')
