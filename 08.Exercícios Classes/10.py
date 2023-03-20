
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        litros = min(litros, self.quantidade_combustivel)
        self.quantidade_combustivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        if litros > self.quantidade_combustivel:
            litros = self.quantidade_combustivel
            valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        return valor

    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro

    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel

    def alterar_quantidade_combustivel(self, quantidade_combustivel):
        self.quantidade_combustivel = quantidade_combustivel


bomba = BombaCombustivel('Gasolina', 5.0, 1000)
print(f'Quantidade de Combustível na Bomba: {bomba.quantidade_combustivel} L')
litros_abastecidos = bomba.abastecer_por_valor(50)
print(f'Litros Abastecidos: {litros_abastecidos} L\n'
      f'Quantidade de Combustível na Bomba: {bomba.quantidade_combustivel} L')
valor_pago = bomba.abastecer_por_valor(10)
print(f'Valor Pago: {locale.currency(valor_pago, grouping=True)}\n'
      f'Quantidade de Combustível na Bomba: {bomba.quantidade_combustivel} L')
bomba.alterar_valor(4.5)
print(f'Novo Valor Litro: {locale.currency(bomba.valor_litro, grouping=True)}')
