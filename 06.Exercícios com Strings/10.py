
from rich import print
unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezenas1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas2 = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
while True:
    try:
        numero = int(input('Número: '))
        if numero < 0 or numero > 99:
            print('[red]ERRO. Número Inválido. Insira um Número de 0 a 99[/]')
        else:
            dezena = numero // 10
            unidade = int(numero % 10)
            if numero >= 20:
                print(dezenas2[dezena], end=' ')
                if unidade != 0:
                    print(f'e {unidades[unidade]}')
            elif numero >= 10:
                print(dezenas1[unidade])
            else:
                print(unidades[unidade])
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Número Inválido. Insira um Número Válido[/]')
