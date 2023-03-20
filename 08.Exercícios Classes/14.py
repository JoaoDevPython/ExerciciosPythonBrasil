
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentar_salario(self, percentual_aumento):
        self.salario *= (1 + percentual_aumento / 100)


harry = Funcionario('Harry', 2500)
print(f'Funcionário: {harry.obter_nome()}\n'
      f'Salário Anterior: {locale.currency(harry.obter_salario(), grouping=True)}')
harry.aumentar_salario(10)
print(f'Novo Salário:     {locale.currency(harry.obter_salario(), grouping=True)}')
