
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
while True:
    try:
        valor = int(input('Saque: Valor Mínimo R$ 10 | Valor Máximo R$ 600: '))
        if valor < 10 or valor > 600:
            print('[red]ERRO. Valor Inválido. Saques: Mínimo R$ 10 e Máximo R$ 600[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
notas = [100, 50, 10, 5, 1]
for nota in notas:
    if valor >= nota:
        saque, valor = divmod(valor, nota)
        print(f'{saque} nota{"" if saque == 1 else "s":1} de {locale.currency(nota, grouping=True)}')
