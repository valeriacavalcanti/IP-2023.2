original = input('Texto: ')

texto = original.upper()
palavras = texto.split()

# identificar os diferentes simbolos (anotador)
distintos = []

for i in range(len(palavras)):
    if (palavras[i] not in distintos):
        distintos.append(palavras[i])

print(distintos)

# calcular a frequência desses símbolos distintos
for i in range(len(distintos)):
    qt = texto.count(distintos[i])
    print('Frequência de', distintos[i], '=', qt)
