numeros = [10,20,30,40,50,60,70,80]
tam = len(numeros)

#invertendo a lista
for i in range(tam//2):
    numeros[i], numeros[tam -1 - i] = numeros[tam -1 - i], numeros[i]

print(numeros)
