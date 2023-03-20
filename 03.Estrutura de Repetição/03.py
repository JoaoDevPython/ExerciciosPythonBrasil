
import locale
import re
from rich import print
from rich.console import Console
from rich.table import Table
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    nome = input('Nome: ').title()
    if len(nome) < 4:
        print('[red]ERRO. Nome Inválido. Insira uma Nome com mais de 3 caracteres[/]')
    elif not re.match(r'^[a-zA-ZÀ-ÿ ]+$', nome):
        print('[red]ERRO. Opção Inválida. Nome deve ser composto apenas por letras[/]')
    else:
        break
while True:
    try:
        idade = int(input('Idade: '))
        if idade < 0 or idade > 150:
            print('[red]ERRO. Idade Inválida. Insira uma Idade de 0 a 150[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Idade Válida[/]')
while True:
    try:
        salario = float(input('Salário: R$ '))
        if salario < 0:
            print('[red]ERRO. Salário Inválido. Insira um Salário Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Salário Válido[/]')
generos = {'F': 'Feminino', 'M': 'Masculino'}
while True:
    sexo = input('Sexo: F ou M: ').upper()
    if sexo not in generos:
        print('[red]ERRO. Sexo Inválido. Responda F ou M[/]')
    else:
        break
estados_civis = {'S': 'Solteiro', 'C': 'Casado', 'V': 'Viúvo', 'D': 'Divorciado'}
while True:
    estado_civil = input('Estado Civil: S, C, V ou D: ').upper()
    if estado_civil not in estados_civis:
        print('[red]ERRO. Estado Civil Inválido. Responda S, C, V ou D[/]')
    else:
        break
tabela = Table('Nome', 'Idade', 'Salário', 'Sexo', 'Estado Civil', header_style='magenta', border_style='cyan')
tabela.add_row(nome, f'{idade}', locale.currency(salario, grouping=True), generos[sexo], estados_civis[estado_civil])
console = Console()
console.print(tabela)
