import random

lista = [0]*10
for i in range(10):
    lista[i] = random.randint(1,100)

print(lista)

qt = 0

numero = int(input("Número: "))
for i in range(10):
    if (numero == lista[i]):
        qt = qt + 1

print(qt)
