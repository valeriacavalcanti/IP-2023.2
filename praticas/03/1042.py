n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

if (n1 > n2) and (n1 > n3):
    maior = n1
    if (n2 > n3):
        meio, menor = n2, n3
    else:
        meio, menor = n3, n2
else:
    if (n2 > n3):
        maior = n2
        if (n1 > n3):
            meio, menor = n1, n3
        else:
            meio, menor = n3, n1
    else:
        maior = n3
        if (n1 > n2):
            meio, menor = n1, n2
        else:
            meio, menor = n2, n1

print(menor, meio, maior, sep='\n')
print()
print(n1, n2, n3, sep='\n')
