n1 = int(input("x: "))
n2 = int(input("y: "))
soma = 0

if (n1 > n2):
    n1, n2 = n2, n1

for i in range(n1 + 1, n2):
    if (i % 2 != 0):
        soma = soma + i

print(soma)
