
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


funcionario = Funcionario('Beatriz', 2000)
print(f'Nome: {funcionario.obter_nome()}\n'
      f'Salário: {locale.currency(funcionario.obter_salario(), grouping=True)}')
