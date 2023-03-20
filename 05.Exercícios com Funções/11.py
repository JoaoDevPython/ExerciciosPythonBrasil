
import re
import datetime
from rich import print
from locale import setlocale, LC_TIME


def data_mes_extenso():
    setlocale(LC_TIME, 'pt_BR')
    while True:
        try:
            data = input('Data (dd/mm/aaaa): ')
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
                print('[red]ERRO. Opção Inválida. Insira uma data no formato dd/mm/aaaa[/]')
            data = datetime.datetime.strptime(data, '%d/%m/%Y')
            situacao = 'Data Futura' if data > datetime.datetime.now() else 'Data Válida'
            print(situacao)
            data_extenso = data.strftime('%d de %B de %Y')
            print(data_extenso)
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('Data Inválida')
        else:
            break


data_mes_extenso()
