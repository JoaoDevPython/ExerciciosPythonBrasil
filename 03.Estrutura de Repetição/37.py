
from rich import print, box
from rich.panel import Panel
clientes = {}
alturas = []
pesos = []
while True:
    try:
        codigo = int(input('(0 = Encerrar) Código do Cliente: '))
        if codigo == 0:
            break
        while True:
            try:
                altura = float(input('Altura em metros: '))
                if altura < 0:
                    print('[red]ERRO. Altura Inválida. Insira uma Altura Positiva[/]')
                else:
                    alturas.append(altura)
                    break
            except KeyboardInterrupt:
                print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
            except ValueError:
                print('[red]ERRO. Insira uma Altura Válida[/]')
        while True:
            try:
                peso = float(input('Peso (kg): '))
                if peso < 0:
                    print('[red]ERRO. Peso Inválido. Insira um Peso Positivo[/]')
                else:
                    pesos.append(peso)
                    break
            except KeyboardInterrupt:
                print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
            except ValueError:
                print('[red]ERRO. Insira um Peso Válido[/]')
        clientes[codigo] = (altura, peso)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Código Válido[/]')
maior_altura = max(clientes, key=lambda x: clientes[x][0])
menor_altura = min(clientes, key=lambda x: clientes[x][0])
maior_peso = max(clientes, key=lambda x: clientes[x][1])
menor_peso = min(clientes, key=lambda x: clientes[x][1])
media_altura = sum(alturas) / len(alturas)
media_pesos = sum(pesos) / len(pesos)
print(Panel(f'Código: {maior_altura}\n'
            f'Altura: {clientes[maior_altura][0]} m',
            title='Cliente mais Alto', box=box.DOUBLE, border_style='green', expand=False))
print(Panel(f'Código: {menor_altura}\n'
            f'Altura: {clientes[menor_altura][0]} m',
            title='Cliente mais Baixo', box=box.DOUBLE, border_style='yellow', expand=False))
print(Panel(f'Código: {maior_peso}\n'
            f'Peso: {clientes[maior_peso][1]} kg',
            title='Cliente mais Gordo', box=box.DOUBLE, border_style='green', expand=False))
print(Panel(f'Código: {menor_peso}\n'
            f'Peso: {clientes[menor_peso][1]} kg',
            title='Cliente mais Magro', box=box.DOUBLE, border_style='yellow', expand=False))
print(Panel(f'Alturas: {media_altura:.2f} m\n'
            f'Pesos:   {media_pesos:.3f} kg',
            title='Média', box=box.DOUBLE, border_style='blue', expand=False))
