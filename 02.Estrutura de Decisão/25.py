
from rich import print
print('Responda: S - Sim ou N - Não')
questionario = ['Telefonou para a vítima?',
                'Esteve no local do crime?',
                'Mora perto da vítima?',
                'Devia para a vítima?',
                'Já trabalhou com a vítima?']
respostas = []
for i in range(5):
    while True:
        resposta = input(f'{questionario[i]}: ').upper()
        if resposta not in ('S', 'N'):
            print('[red]ERRO. Resposta Inválida. Responda S ou N[/]')
        else:
            respostas.append(resposta)
            break
sim = respostas.count('S')
classificacao = 'Inocente' if sim < 2 else 'Suspeita(o)' if sim < 3 else 'Cúmplice' if sim < 5 else 'Assassina(o)'
print(classificacao)
