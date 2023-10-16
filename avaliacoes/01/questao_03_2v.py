qt = 0

n1 = int(input("Valor1: "))

while (True):
    n2 = int(input("Valor2: "))
    
    if (n2 > n1):
        break

    qt += 1


print(qt, 'numeros lidos')
print('n1 = {}'.format(n1))
print('n2 = {}'.format(n2))

