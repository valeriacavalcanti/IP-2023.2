texto = input('Texto: ')

qt = 0

for i in range(len(texto)):
    if (texto[i] == ' '):
        qt = qt + 1

qt = qt + 1

print('Quantidade de palavras:', qt)
