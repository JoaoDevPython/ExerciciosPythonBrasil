
import locale
from rich import print
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def valor_pagamento(valor_prestacao, dias_atraso):
    pagamentos = valor_prestacao
    if dias_atraso > 0:
        multa = 0.03
        juros = 0.001
        pagamentos = valor_prestacao + (valor_prestacao * multa) + (valor_prestacao * juros * dias_atraso)
    return pagamentos


total_prestacoes = valor_total = 0
while True:
    try:
        prestacao = float(input('(0 = Encerrar) Valor da Prestação: R$ '))
        if prestacao == 0:
            break
        atraso = int(input('Dias de Atraso: '))
        pagamento = valor_pagamento(prestacao, atraso)
        print(f'Valor a ser Pago: {locale.currency(pagamento, grouping=True)}')
        total_prestacoes += 1
        valor_total += pagamento
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira um Valor Válido[/]')
print(f'Relatório do Dia\n'
      f'Quantidade de Prestações: {total_prestacoes}\n'
      f'Valor Total: {locale.currency(valor_total, grouping=True)}')
