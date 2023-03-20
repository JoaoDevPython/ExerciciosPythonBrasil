
import locale
from rich import print
from rich.panel import Panel
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
carnes = {1: 'Filé Duplo', 2: 'Alcatra', 3: 'Picanha'}
while True:
    try:
        opcao = int(input('Carnes: 1 - Filé Duplo, 2 - Alcatra ou 3 - Picanha: '))
        if opcao not in carnes:
            print('[red]ERRO. Insira um Número. Opção: 1, 2 ou 3[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Número Válido[/]')
while True:
    try:
        peso = float(input('Peso Carne (kg): '))
        if peso < 0:
            print('[red]ERRO. Peso Inválido. Insira um Peso Positivo[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Peso Válido[/]')
pagamentos = {4: 'Cartão Tabajara', 5: 'Dinheiro'}
while True:
    try:
        pagamento = int(input('Forma de Pagamento: 4 - Cartão Tabajara ou 5 - Dinheiro: '))
        if pagamento not in pagamentos:
            print('[red]Erro. Insira um Pagamento. Opção: 4 ou 5[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]Erro. Insira um Pagamento Válido[/]')
desconto = preco = 0
if opcao == 1:
    preco = peso * 4.9 if peso <= 5 else peso * 5.8
elif opcao == 2:
    preco = peso * 5.9 if peso <= 5 else peso * 6.8
elif opcao == 3:
    preco = peso * 6.9 if peso <= 5 else peso * 7.8
if pagamento == 4:
    desconto = preco * 0.05
valor = preco - desconto
print(Panel(f'Tipo de Carne:     {carnes[opcao]}\n'
            f'Quantidade:        {peso:.3f} kg\n'
            f'Preço Total:       [green]{locale.currency(preco, grouping=True)}[/]\n'
            f'Tipo de Pagamento: {pagamentos[pagamento]}\n'
            f'Valor do Desconto: [red]{locale.currency(desconto, grouping=True)}[/]\n'
            f'Valor a Pagar:     [blue]{locale.currency(valor, grouping=True)}[/]',
            title='Cupom Fiscal', border_style='cyan', expand=False))
