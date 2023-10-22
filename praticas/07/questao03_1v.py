import random

lista = [0]*10
for i in range(10):
    lista[i] = random.randint(1,100)

print(lista)

existe = False

numero = int(input("Número: "))
for i in range(10):
    if (numero == lista[i]):
        existe = True
        break

if (existe == True):
    print("Existe, no índice", i)
else:
    print("Nao existe")
