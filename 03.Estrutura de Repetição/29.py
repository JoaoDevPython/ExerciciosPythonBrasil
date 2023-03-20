
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print('Loja Quase Dois - Tabela de Preços')
for i in range(1, 51):
    preco = i * 1.99
    print(f'{i:2} - {locale.currency(preco, grouping=True)}')
