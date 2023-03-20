
from rich import print
while True:
    try:
        a = float(input('1º Lado: '))
        b = float(input('2º Lado: '))
        c = float(input('3º Lado: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Lado Válido[/]')
if a + b < c or a + c < b or b + c < a:
    print('Não é um Triângulo')
elif a == b and a == c:
    print('Equilátero')
elif a == b or a == c or b == c:
    print('Isósceles')
else:
    print('Escaleno')
