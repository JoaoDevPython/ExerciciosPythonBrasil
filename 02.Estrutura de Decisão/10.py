
from rich import print
turnos = {'M': {'turno': 'Matutino', 'saudacao': 'Bom Dia!'},
          'V': {'turno': 'Vespertino', 'saudacao': 'Boa Tarde!'},
          'N': {'turno': 'Noturno', 'saudacao': 'Boa Noite!'}}
while True:
    try:
        turno = input('Turno: M, V ou N: ').upper()
        if turno not in turnos:
            print('[red]ERRO. Insira a letra M, V ou N[/]')
        else:
            break
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma letra[/]')
print(f'{turnos[turno]["turno"]}\n'
      f'{turnos[turno]["saudacao"]}')
