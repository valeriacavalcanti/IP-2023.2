cod = int(input('Código: '))
qtde = int(input('Quantidade: '))

valor = 0

if (cod == 1):
    valor = qtde * 4.0
else:
    if (cod == 2):
        valor = qtde * 4.5
    else:
        if (cod == 3):
            valor = qtde * 5.0
        else:
            if (cod == 4):
                valor = qtde * 2.0
            else:
                valor = qtde * 1.5

print('Total: R$ {:.2f}'.format(valor))
