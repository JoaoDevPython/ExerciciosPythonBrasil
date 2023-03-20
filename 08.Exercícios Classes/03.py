
class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def muda_lado_a(self, novo_lado):
        self.lado_a = novo_lado

    def muda_lado_b(self, novo_lado):
        self.lado_b = novo_lado

    def retorna_lado_a(self):
        return self.lado_a

    def retorna_lado_b(self):
        return self.lado_b

    def calcula_area(self):
        return self.lado_a * self.lado_b

    def calcula_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


comprimento = float(input('Comprimento do Local: '))
largura = float(input('Largura do Local: '))
altura_piso = float(input('Altura do Piso: '))
altura_rodape = float(input('Altura do Rodapé: '))
area_local = Retangulo(comprimento, largura).calcula_area()
area_piso = Retangulo(altura_piso, altura_piso).calcula_area()
area_rodape = Retangulo(altura_rodape, altura_rodape).calcula_area()
quantidade_pisos = area_local / area_piso
quantidade_rodapes = Retangulo(comprimento, altura_rodape).calcula_perimetro() / altura_rodape
print(f'Serão Necessários {quantidade_pisos} Pisos e {quantidade_rodapes} Rodapés para o Local')
