
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


pessoa = Pessoa('Ana', 20, 70, 1.70)
print(f'Antes:\n'
      f'Idade:  {pessoa.idade}\n'
      f'Peso:   {pessoa.peso} kg\n'
      f'Altura: {pessoa.altura} m')
pessoa.envelhecer()
pessoa.engordar(5)
pessoa.emagrecer(3)
pessoa.crescer(0.1)
print(f'Depois:\n'
      f'Idade:  {pessoa.idade}\n'
      f'Peso:   {pessoa.peso} kg\n'
      f'Altura: {pessoa.altura} m')
