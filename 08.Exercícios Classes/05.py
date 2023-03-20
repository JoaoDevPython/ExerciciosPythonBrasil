
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo Insuficiente')


conta = ContaCorrente(555, 'Maria')
print(f'Saldo Inicial: {locale.currency(conta.saldo, grouping=True)}')
conta.deposito(100)
print(f'Saldo Após Deposito: {locale.currency(conta.saldo, grouping=True)}')
conta.saque(50)
print(f'Saldo Após Saque: {locale.currency(conta.saldo, grouping=True)}')
conta.alterar_nome('Fernanda')
print(f'Nome do Correntista: {conta.nome_correntista}')
