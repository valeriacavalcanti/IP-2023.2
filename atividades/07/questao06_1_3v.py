# SOLUÇÃO USANDO LISTA
# SEM OPERADOR IN
# CONSIDERANDO QUE LETRAS MAIÚSCULAS E MINÚSCULAS SÃO DIFERENTES

texto = input('Texto: ')
distintos = []

for i in range(len(texto)):
    existe = False
    for j in range(len(distintos)):
        if (texto[i] == distintos[j]):
            existe = True
            break
    if (existe == False):
        distintos.append(texto[i])

print('Distintos:', distintos)

