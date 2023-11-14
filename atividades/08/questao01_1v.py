original = input('Informe o texto: ')

texto = original.lower()

# identificar os diferentes simbolos (anotador)
distintos = []

for i in range(len(texto)):
    if (texto[i] not in distintos):
        distintos.append(texto[i])

print(distintos)

# calcular a frequência desses símbolos distintos
for i in range(len(distintos)):
    qt = texto.count(distintos[i])
    print('Frequência de', distintos[i], '=', qt)
