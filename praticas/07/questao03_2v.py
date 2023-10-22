import random

lista = [0]*10
for i in range(10):
    lista[i] = random.randint(1,100)

print(lista)

numero = int(input("Número: "))
for i in range(10):
    if (numero == lista[i]):
        break

if (i < 9):
    print("Existe, no índice", i)
elif (numero == lista[9]):
    print("Existe, no índice 9")
else:
    print("Nao existe")
