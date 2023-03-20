
from rich import print
while True:
    usuario = input('Usuário: ')
    senha = input('Senha: ')
    if usuario == senha:
        print('[red]ERRO. Usuário e Senha não devem ser iguais[/]')
    else:
        break
