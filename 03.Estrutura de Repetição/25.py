
from rich import print
while True:
    try:
        quantidade = int(input('Quantidade de Pessoas: '))
        break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Quantidade Válida[/]')
idades = []
for i in range(quantidade):
    while True:
        try:
            idades.append(int(input(f'{i + 1}ª Pessoa | Idade: ')))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Idade Válida[/]')
media = sum(idades) / len(idades)
turma = 'Jovem' if media < 26 else 'Adulta' if media < 61 else 'Idosa'
print(f'Turma: {turma}')
