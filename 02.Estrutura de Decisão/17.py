
from rich import print
while True:
    try:
        ano = int(input('Ano: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Ano Válido[/]')
bissexto_ou_nao = 'Bissexto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'Não é Bissexto'
print(bissexto_ou_nao)
