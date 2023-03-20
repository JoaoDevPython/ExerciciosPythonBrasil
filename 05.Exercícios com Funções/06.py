
from rich import print


def conversao_horario(hora, minuto):
    periodo = 'A.M.' if hora < 12 else 'P.M.'
    hora = hora if hora <= 12 else hora - 12
    hora = hora if hora != 0 else 12
    return hora, minuto, periodo


def imprimir_horario(hora, minuto, periodo):
    print(f'{hora}:{minuto:02} {periodo}')


while True:
    try:
        horas = int(input('Hora (0 - 23): '))
        if horas < 0 or horas > 23:
            print('[red]ERRO. Hora Inválida. Insira Hora de 0 a 23[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Hora Válida[/]')
while True:
    try:
        minutos = int(input('Minuto (0 - 59): '))
        if minutos < 0 or minutos > 59:
            print('[red]ERRO. Minuto Inválido. Insira Minuto de 0 a 59[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Minuto Válido[/]')
h, m, p = conversao_horario(horas, minutos)
imprimir_horario(h, m, p)
