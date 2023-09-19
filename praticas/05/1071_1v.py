n1 = int(input("x: "))
n2 = int(input("y: "))
soma = 0

if (n1 > n2):
    for i in range(n1 - 1, n2, -1):
        if (i % 2 != 0):
            soma = soma + i
else:
    for i in range(n1 + 1, n2):
        if (i % 2 != 0):
            soma = soma + i

print(soma)
