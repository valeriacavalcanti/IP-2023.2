original = input('Informe o texto: ')

texto = original.lower()

# identificar os diferentes simbolos (anotador)
distintos = []
frequencia = []

for i in range(len(texto)):
    if (texto[i] not in distintos):
        distintos.append(texto[i])
        frequencia.append(1)
    else:
        for j in range(len(distintos)):
            if (texto[i] == distintos[j]):
                break
        frequencia[j] += 1
        #indice = distintos.index(texto[i])
        #frequencia[indice] += 1


#print(distintos)
#print(frequencia)

for i in range(len(distintos)):
    print(distintos[i], '=', frequencia[i])
