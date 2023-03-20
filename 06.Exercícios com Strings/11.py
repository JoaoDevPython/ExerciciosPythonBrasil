
from rich import print
from random import choice
with open('palavras.txt', 'r', encoding='UTF-8') as palavrasTXT:
    print('[cyan]Bem-Vindo ao Jogo da Forca[/]\n'
          'Uma palavra aleatória já foi escolhida\n'
          'Você tem 6 tentativas')
    palavras = [palavra.replace('\n', '') for palavra in palavrasTXT]
palavra_escolhida = choice(palavras)
letras_erradas = []
lista_palavra_escolhida = []
lista_palavra_oculta = []
lista_letras_certas = []
tentativas = 0
for letra in palavra_escolhida:
    lista_palavra_escolhida.append(letra)
    lista_palavra_oculta.append('_')
while tentativas <= 6:
    print(f'A palavra é: {" ".join(lista_palavra_oculta)}\n'
          f'Letras erradas: {" ".join(letras_erradas)}')
    letra = input('Letra: ')
    letra = letra.casefold()
    if len(letra) != 1:
        print('[red]ERRO. Digite apenas uma Letra[/]')
        continue
    elif letra in letras_erradas:
        print('[yellow]Você já digitou esta Letra[/]')
        continue
    if letra in palavra_escolhida:
        if letra in lista_letras_certas:
            print('[yellow]Você já digitou esta Letra[/]')
            continue
        for i, nova_letra in enumerate(lista_palavra_escolhida):
            if letra == nova_letra:
                lista_palavra_oculta[i] = letra
                lista_letras_certas.append(lista_palavra_oculta[i])
        if '_' not in lista_palavra_oculta:
            print(f'[green]:trophy:Parabéns! Você acertou!:grin:[/]\n'
                  f'Palavra: [cyan]"{palavra_escolhida}"[/]')
            break
    else:
        if tentativas == 6:
            print(f'[red]:rage:Infelizmente você perdeu!:sob:[/] A palavra era: [cyan]"{palavra_escolhida}"[/]')
            break
        letras_erradas.append(letra)
        tentativas += 1
        print(f'[red]Você Errou pela {tentativas}ª vez! Tente novamente![/]')
