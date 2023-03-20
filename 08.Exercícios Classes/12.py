
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class ContaInvestiento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicione_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    def obter_saldo(self):
        return self.saldo


poupanca = ContaInvestiento(1000, 10)
for _ in range(5):
    poupanca.adicione_juros()
print(f'Saldo Após 5 Meses: {locale.currency(poupanca.obter_saldo(), grouping=True)}')
