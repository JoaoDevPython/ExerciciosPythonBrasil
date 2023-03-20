
from math import sqrt
from rich import print
while True:
    try:
        a = int(input('Coeficiente de A: '))
        if a == 0:
            print('[red]ERRO. Coeficiente A = 0, não é uma equação de 2º grau[/]\n'
                  'Programa Encerrado')
        else:
            b = int(input('Coeficiente de B: '))
            c = int(input('Coeficiente de C: '))
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                print('Delta menor que 0. Raízes Imaginárias')
            elif delta == 0:
                raiz = - b / 2 * a
                print(f'Delta igual a 0.\n'
                      f'Raiz: {raiz}')
            else:
                raiz1 = (- b + sqrt(delta) / 2 * a)
                raiz2 = (- b - sqrt(delta) / 2 * a)
                print(f'Raízes: {raiz1} | {raiz2}')
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Coeficiente Válido[/]')
