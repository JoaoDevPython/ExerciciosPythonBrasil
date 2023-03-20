
from rich import print
from random import choice, shuffle
with open('palavras.txt', 'r', encoding='UTF-8') as palavrasTXT:
    palavras = []
    for palavra in palavrasTXT:
        palavras.append(palavra.replace('\n', ''))
palavra = choice(palavras)
lista_palavra = list(palavra)
shuffle(lista_palavra)
tentativas = 0
while tentativas < 3:
    print(f'Palavra Embaralhada: [blue]{" ".join(lista_palavra)}[/]')
    resposta = input('Palavra Certa: ')
    if resposta == palavra:
        print('[green]:trophy:Parabéns! Você Acertou!:grin:[/]')
        break
    else:
        tentativas += 1
        if tentativas == 3:
            print(f'[red]:rage:Você Perdeu!:sob:[/]\n'
                  f'Palavra: [cyan]"{palavra}"[/]')
            break
        else:
            print(f'[red]Você Errou!\n'
                  f'Tentativas: {tentativas}[/]')
