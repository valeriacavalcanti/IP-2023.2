# SOLUÇÃO USANDO LISTA
# COM OPERADOR IN
# CONSIDERANDO QUE LETRAS MAIÚSCULAS E MINÚSCULAS SÃO DIFERENTES

texto = input('Texto: ')
distintos = []

for i in range(len(texto)):
    if (texto[i] not in distintos):
        distintos.append(texto[i])

print('Distintos:', distintos)

