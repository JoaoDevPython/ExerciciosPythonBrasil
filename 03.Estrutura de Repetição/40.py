
from rich import print
cidades = []
for i in range(5):
    while True:
        try:
            print(f'Dados da Cidade {i + 1}')
            codigo = int(input('Código da Cidade: '))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Código Válido[/]')
    while True:
        try:
            veiculos = int(input('Número de Veiculos de Passeio (em 1999): '))
            if veiculos < 0:
                print('[red]ERRO. Número Inválido. Insira um Número Positivo[/]')
            else:
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
    while True:
        try:
            acidentes = int(input('Número de Acidentes de Trânsito com Vítimas (em 1999): '))
            if acidentes < 0:
                print('[red]ERRO. Número Inválido. Insira um Número Positivo[/]')
            else:
                cidades.append([codigo, veiculos, acidentes])
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
maior_indice = cidades.index(max(cidades, key=lambda x: x[2]))
menor_indice = cidades.index(min(cidades, key=lambda x: x[2]))
media_veiculos = sum(cidade[1] for cidade in cidades) / 5
print(f'Maior Índice de Acidentes:\n'
      f'Código: {cidades[maior_indice][0]}\n'
      f'Acidentes: {cidades[maior_indice][2]}\n\n'
      f'Menor Índice de Acidentes:\n'
      f'Código: {cidades[menor_indice][0]}\n'
      f'Acidentes: {cidades[menor_indice][2]}\n\n'
      f'Média de Veículos nas Cidades: {media_veiculos}')
if menos_2000_veiculos := [cidade[2] for cidade in cidades if cidade[1] < 2000]:
    media_menos_2000_veiculos = sum(menos_2000_veiculos) / len(menos_2000_veiculos)
    print(f'Média de Acidentes de Trânsito nas Cidades com menos de 2000 veículos: {media_menos_2000_veiculos}')
else:
    print('Não há Cidades com menos de 2000 Veículos de Passeio')
