n1 = int(input("N1: "))
n2 = int(input("N2: "))

if (n1 > n2):
    n1, n2 = n2, n1

if (n2 % n1 == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
