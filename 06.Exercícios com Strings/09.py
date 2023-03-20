
import re
cpf = input('Insira um CPF (xxx.xxx.xxx-xx): ')
if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
    print('CPF inválido')
else:
    digitos = [int(d) for d in cpf if d.isdigit()]
    numeracao = 10
    somatorio = 0
    for i in range(9):
        somatorio += numeracao * digitos[i]
        numeracao -= 1
    restante = somatorio % 11
    verificar_primeiro_digito = 0 if restante < 2 else 11 - restante
    numeracao = 11
    somatorio = 0
    for i in range(9, len(digitos) - 1):
        somatorio += numeracao * digitos[i]
        numeracao -= 1
    somatorio += verificar_primeiro_digito * 2
    restante = somatorio % 11
    verificar_segundo_digito = 0 if restante < 2 else 11 - restante
    if verificar_primeiro_digito != digitos[9] or verificar_segundo_digito != digitos[10]:
        print('CPF Inválido')
    else:
        print('CPF válido')
