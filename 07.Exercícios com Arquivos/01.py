
import socket
from rich.console import Console
from rich.table import Table


def validar(endereco_ip: str):
    try:
        socket.inet_aton(endereco_ip)
        return True
    except socket.error:
        return False


ips_validos = []
ips_invalidos = []
with open('enderecosIP.txt', 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)
tabela = Table('Endereços Válidos', 'Endereços Inválidos')
for ip_val in ips_validos:
    tabela.add_row(ip_val, '')
for ip_inv in ips_invalidos:
    tabela.add_row('', ip_inv)
console = Console(record=True)
try:
    with open('relatorioIP.txt', 'w', encoding='utf-8') as arquivo:
        console.print(tabela)
        conteudo = console.export_text()
        arquivo.write(conteudo)
except IOError:
    print('Ocorreu um Erro ao Gravar o Arquivo')
