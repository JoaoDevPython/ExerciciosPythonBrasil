
from rich import print
idades = []
alturas = []
for i in range(5):
    while True:
        try:
            idade = int(input(f'{i + 1}ª Pessoa | Idade: '))
            if idade < 0:
                print('[red]ERRO. Idade Inválida. Insira uma Idade Positiva[/]')
            else:
                idades.append(idade)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Idade Válida[/]')
    while True:
        try:
            altura = float(input(f'{i + 1}ª Pessoa | Altura em Metros: '))
            if altura < 0:
                print('[red]ERRO. Altura Inválida. Insira uma Altura Positiva[/]')
            else:
                alturas.append(altura)
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Altura Válida[/]')
idades.reverse()
alturas.reverse()
print(f'Idades: {", ".join(map(str, idades))}\n'
      f'Alturas: {", ".join(map(str, alturas))}')
