import random

lista = [0]*10
for i in range(10):
    lista[i] = random.randint(1,100)

print(lista)

maior = lista[0]
for i in range(1,10):
    if (lista[i] > maior):
        maior = lista[i]

print(maior)
