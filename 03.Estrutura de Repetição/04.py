
pais_a = 80000
taxa_a = 1.03
pais_b = 200000
taxa_b = 1.015
anos = 0
while pais_a < pais_b:
    anos += 1
    pais_a *= taxa_a
    pais_b *= taxa_b
    print(f'Ano {anos}\n'
          f'País A: {pais_a:.0f}\n'
          f'País B: {pais_b:.0f}\n')
print(f'Ultrapassa em {anos} anos')
