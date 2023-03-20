
from rich import print
numeros = []
for i in range(2):
    while True:
        try:
            numeros.append(float(input(f'{i + 1}º Número: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
operacoes = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}
while True:
    opcao = input('Operações: + [Adição] | - [Subtração] | * [Multiplicação] | / [Divisão]: ')
    if opcao not in operacoes:
        print('[red]ERRO. Insira uma Operação. Ex.: +, -, * ou /[/]')
        continue
    elif opcao == '/' and numeros[0] == 0 or numeros[1] == 0:
        print('[red]ERRO. Não é possível dividir por 0[/]')
        break
    resultado = operacoes[opcao](numeros[0], numeros[1])
    par_impar = 'Par' if resultado % 2 == 0 else 'Ímpar'
    positivo_negativo = 'Positivo' if resultado > 0 else 'Negativo' if resultado < 0 else 'Nulo'
    inteiro_decimal = 'Inteiro' if resultado % 1 == 0 else 'Decimal'
    print(f'{numeros[0]} {opcao} {numeros[1]} = {resultado}\n'
          f'{par_impar}\n'
          f'{positivo_negativo}\n'
          f'{inteiro_decimal}')
    break
