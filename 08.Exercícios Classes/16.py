
class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def __str__(self):
        return (f'Bichinho: {self.nome}\n'
                f'Fome:  {self.fome}\n'
                f'Saúde: {self.saude}\n'
                f'Idade: {self.idade}\n'
                f'Tédio: {self.tedio}')

    def ver_fome(self):
        return self.fome

    def ver_saude(self):
        return self.saude

    def ver_idade(self):
        return self.idade

    def ver_tedio(self):
        return self.tedio

    def alimentar(self, comida):
        self.fome -= comida

    def brincar(self, tempo):
        self.tedio -= tempo

    def envelhecer(self):
        self.idade += 1
        self.fome += 5
        self.saude -= 10
        self.tedio += 5


meu_bichinho = Bichinho('Pikachu')
meu_bichinho.alimentar(10)
meu_bichinho.brincar(30)
print(meu_bichinho)
