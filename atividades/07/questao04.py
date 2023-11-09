texto = input('Texto: ')

qt = 0

for i in range(len(texto)):
    if (texto[i] >= 'A') and (texto[i] <= 'Z'):
        qt = qt + 1

print('Quantidade de letras maiúsculas:', qt)
