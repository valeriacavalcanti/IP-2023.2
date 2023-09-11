a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

# descobrir o maior dos lados

if (a > b) and (a > c):
    maior = a
    lado2 = b
    lado3 = c
else:
    if (b > c):
        maior = b
        lado2 = a
        lado3 = c
    else:
        maior = c
        lado2 = a
        lado3 = b

# verificar se forma triangulo
if (maior >= lado2 + lado3):
    print('NAO FORMA TRIANGULO')
else:
    # verificar o tipo (ângulo)
    if (maior ** 2 == (lado2 ** 2) + (lado3 ** 2)):
        print('TRIANGULO RETANGULO')
    else:
        if (maior ** 2 > (lado2 ** 2) + (lado3 ** 2)):
            print('TRIANGULO OBTUSANGULO')
        else:
            print('TRIANGULO ACUTANGULO')

    # verificar o tipo (medida)
    if (maior == lado2) and (maior == lado3):
        print('TRIANGULO EQUILATERO')
    else:
        if (maior == lado2) or (maior == lado3) or (lado2 == lado3):
            print('TRIANGULO ISOSCELES')
