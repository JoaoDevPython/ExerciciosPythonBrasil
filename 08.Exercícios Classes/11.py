
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        consumo = distancia / self.consumo
        if consumo > self.combustivel:
            print('Combustível Insuficiente para Percorrer a Distância Desejada')
        else:
            self.combustivel -= consumo

    def obter_gasolina(self):
        return self.combustivel

    def adicionar_gasolina(self, quantidade):
        self.combustivel += quantidade


meu_fusca = Carro(15)
meu_fusca.adicionar_gasolina(20)
meu_fusca.andar(100)
print(f'Combustível Restante: {meu_fusca.obter_gasolina():.2f} L')
