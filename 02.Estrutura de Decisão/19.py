
from rich import print
while True:
    try:
        numero = int(input('Número: '))
        if numero < 1 or numero > 999:
            print('[red]ERRO. Insira um Número Positivo de 1 a 999[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
print(f'{centena} centena{"" if centena == 1 else "s"}, '
      f'{dezena} dezena{"" if dezena == 1 else "s"} e '
      f'{unidade} unidade{"" if unidade == 1 else "s"}')
