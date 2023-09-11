a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

# ordenação

if (a > b) and (a > c):
    if (b > c):
        a, b, c = a, b, c
    else:
        a, b, c = a, c, b
elif (b > c):
    if (a > c):
        a, b, c = b, a, c
    else:
        a, b, c = b, c, a
else:
    if (a > b):
        a, b, c = c, a, b
    else:
        a, b, c = c, b, a

# verificar se forma triangulo
if (a >= b + c):
    print('NAO FORMA TRIANGULO')
else:
    # verificar o tipo (ângulo)
    if (a ** 2 == b ** 2 + c ** 2):
        print('TRIANGULO RETANGULO')
    elif (a ** 2 > b ** 2 + c ** 2):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    # verificar o tipo (medida)
    if (a == b) and (a == c):
        print('TRIANGULO EQUILATERO')
    elif (a == b) or (a == c) or (b == c):
        print('TRIANGULO ISOSCELES')
