# SOLUÇÃO USANDO LISTA
# SEM OPERADOR IN
# CONSIDERANDO QUE LETRAS MAIÚSCULAS E MINÚSCULAS SÃO IGUAIS

texto = input('Texto: ')
distintos = []

for i in range(len(texto)):
    if (texto[i] >= 'a') and (texto[i] <= 'z'):
        s = chr(ord(texto[i]) - 32)
    else:
        s = texto[i]

    existe = False
    for j in range(len(distintos)):
        if (s == distintos[j]):
            existe = True
            break
    if (existe == False):
        distintos.append(s)

print('Distintos:', distintos)

