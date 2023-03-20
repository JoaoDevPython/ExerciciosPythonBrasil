
import random
from rich import print


def jogo_craps():
    print('[cyan]Bem-Vindo ao Jogo de Craps[/]')
    jogada_inicial = random.randint(2, 12)
    print(f'Você tirou {jogada_inicial} na sua 1ª jogada')
    if jogada_inicial in {7, 11}:
        print('[green]:trophy:Você é um "Natural" e ganhou!:grin:[/]')
        return
    elif jogada_inicial in {2, 3, 12}:
        print('[red]:rage:Você é um "Craps" e perdeu!:sob:[/]')
        return
    else:
        ponto = jogada_inicial
        print(f'Seu ponto é {ponto}')

    while True:
        nova_jogada = random.randint(2, 12)
        print(f'Você tirou {nova_jogada}')
        if nova_jogada == 7:
            print('[red]:rage:Você perdeu! Pois tirou 7 antes de seu ponto:sob:[/]')
            break
        elif nova_jogada == ponto:
            print('[green]:trophy:Parabéns! Você ganhou!:grin:[/]')
            break


print('[cyan]Vamos Jogar![/]')
jogo_craps()
