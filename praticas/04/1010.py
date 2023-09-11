cod1 = int(input("Código peça 1: "))
qt1 = int(input('Qtd peça 1: '))
valor1 = float(input('Valor peça 1: '))

cod2 = int(input("Código peça 2: "))
qt2 = int(input('Qtd peça 2: '))
valor2 = float(input('Valor peça 2: '))

total = (qt1 * valor1) + (qt2 * valor2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
