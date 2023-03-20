
class BichinhoVirtual:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, valor):
        self.fome += valor

    def alterar_saude(self, valor):
        self.saude += valor

    def alterar_idade(self, valor):
        self.idade += valor

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        return (self.fome + self.saude) / 2


fofinho = BichinhoVirtual('Fofinho')
fofinho.alterar_nome('Fofucho')
fofinho.alterar_fome(10)
fofinho.alterar_saude(-10)
fofinho.alterar_idade(1)
print(f'Humor: {fofinho.calcular_humor()}')
