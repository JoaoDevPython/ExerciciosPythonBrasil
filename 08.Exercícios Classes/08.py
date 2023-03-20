
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        print(f'O bucho do macaco {self.nome} contém {", ".join(self.bucho)}')

    def digerir(self):
        self.bucho = []
        print(f'O macaco {self.nome} digeriu tudo e agora está com o bucho vazio')


macaco1 = Macaco('Chico')
macaco2 = Macaco('Zé')
macaco1.comer('Banana')
macaco1.comer('Maçã')
macaco2.comer('Cenoura')
macaco1.ver_bucho()
macaco2.ver_bucho()
macaco1.digerir()
macaco2.digerir()
