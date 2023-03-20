
from rich import print, box
from rich.panel import Panel
alunos = []
for i in range(10):
    while True:
        try:
            numero = int(input(f'Número do {i + 1}º Aluno: '))
            break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira um Número Válido[/]')
    while True:
        try:
            altura = int(input(f'Altura em cm do {i + 1}º Aluno: '))
            if altura < 0:
                print('[red]ERRO. Altura Inválida. Insira uma Altura Positiva[/]')
            else:
                alunos.append((numero, altura))
                break
        except KeyboardInterrupt:
            print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
        except ValueError:
            print('[red]ERRO. Insira uma Altura Válida[/]')
maior_altura = max(alunos, key=lambda x: x[1])
menor_altura = min(alunos, key=lambda x: x[1])
print(Panel(f'Número: {maior_altura[0]}\n'
            f'Altura: {maior_altura[1]} m',
            title='Aluno mais Alto', box=box.DOUBLE, border_style='green', expand=False))
print(Panel(f'Número: {menor_altura[0]}\n'
            f'Altura: {menor_altura[1]} m',
            title='Aluno mais Baixo', box=box.DOUBLE, border_style='yellow', expand=False))
