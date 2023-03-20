
from rich import print
notas = []
while True:
    try:
        nota = float(input('(-1 = Encerrar) Nota: '))
        if nota == -1:
            break
        elif nota < 0 or nota > 10:
            print('[red]ERRO. Nota Inválida. Insira uma Nota de 0 a 10[/]')
        else:
            notas.append(nota)
    except KeyboardInterrupt:
        print('[red]ERRO. Entrada Interrompida pelo Usuário[/]')
    except ValueError:
        print('[red]ERRO. Insira uma Nota Válida[/]')
soma = sum(notas)
media = sum(notas) / len(notas)
print(f'Quantidade de Valores Lidos: {len(notas)}\n'
      f'Notas em Ordem: {", ".join(map(str, notas))}')
notas.reverse()
print(f'Notas em Ordem Inversa: {", ".join(map(str, notas))}\n'
      f'Soma: {soma}\n'
      f'Média: {media:.2f}')
acima_media = []
abaixo_sete = []
for nota_ in notas:
    if nota_ > media:
        acima_media.append(nota_)
    if nota_ < 7:
        abaixo_sete.append(nota_)
print(f'Quantidade de Valores Acima da Média: {len(acima_media)}\n'
      f'Quantidade de Valores Abaixo de 7: {len(abaixo_sete)}\n'
      f'Programa Encerrado')
