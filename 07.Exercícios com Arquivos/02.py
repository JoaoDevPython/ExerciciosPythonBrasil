
from rich.console import Console
from rich.table import Table


def transformar_megabytes(tamanho_bytes: str):
    return int(tamanho_bytes) / (2 ** 10) ** 2


lista_dados = []
with open('usuarios.txt', 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_disco = transformar_megabytes(linha[16:])
        lista_dados.append((usuario, tamanho_disco))
tabela = Table(title='Acme Inc.\tUso do espaço em disco pelos usuários')
tabela.add_column('Nr.')
tabela.add_column('Usuário')
tabela.add_column('Espaço Utilizado', justify='right')
tabela.add_column('% do uso', justify='right')
tamanho_total = sum(tamanho for _, tamanho in lista_dados)
for indice, dados in enumerate(lista_dados, start=1):
    usuario, tamanho_disco = dados
    percentual = tamanho_disco / tamanho_total
    tabela.add_row(f'{indice}', usuario, f'{tamanho_disco:.2f} MB', f'{percentual:.2%}')
media = tamanho_total / len(lista_dados)
console = Console(record=True)
try:
    with open('relatorio.txt', 'w', encoding='utf-8') as arquivo:
        console.print(tabela)
        console.print(f'Espaço Total Ocupado: {tamanho_total:.2f} MB')
        console.print(f'Espaco Médio Ocupado:  {media:.2f} MB')
        conteudo = console.export_text()
        arquivo.write(conteudo)
except IOError:
    print('Ocorreu um Erro ao Gravar o Arquivo')
