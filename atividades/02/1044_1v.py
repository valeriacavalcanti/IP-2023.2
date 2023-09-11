n1 = int(input("N1: "))
n2 = int(input("N2: "))

if (n1 > n2):
    menor, maior = n2, n1
else:
    menor, maior = n1, n2


if (maior % menor == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
