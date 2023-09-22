qtd_rato = 0
qtd_sapo = 0
qtd_coelho = 0

qtd_exp = int(input())

for i in range(qtd_exp):
    qtd, tipo = input().split()
    qtd = int(qtd)

    if (tipo == 'C'):
        qtd_coelho = qtd_coelho + qtd
    elif (tipo == 'S'):
        qtd_sapo = qtd_sapo + qtd
    else:
        qtd_rato = qtd_rato + qtd

total = qtd_rato + qtd_sapo + qtd_coelho
p_coelho = (qtd_coelho/total) * 100
p_rato = (qtd_rato/total) * 100
p_sapo = (qtd_sapo/total) * 100

# Total: 92 cobaias
print('Total:', total, 'cobaias')

# Total de coelhos: 29
print('Total de coelhos:', qtd_coelho)

# Total de ratos: 40
print('Total de ratos:', qtd_rato)

# Total de sapos: 23
print('Total de sapos:', qtd_sapo)

# Percentual de coelhos: 31.52 %
print('Percentual de coelhos: {:.2f} %'.format(p_coelho))

# Percentual de ratos: 43.48 %
print('Percentual de ratos: {:.2f} %'.format(p_rato))

# Percentual de sapos: 25.00 %
print('Percentual de sapos: {:.2f} %'.format(p_sapo))
