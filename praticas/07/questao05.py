import random

lista = [0]*10
for i in range(10):
    lista[i] = random.randint(1,100)

print(lista)

numero = int(input("Número: "))
for i in range(10):
    if (lista[i] > numero):
        print(lista[i])
