# SOLUÇÃO USANDO LISTA
# COM OPERADOR IN
# CONSIDERANDO QUE LETRAS MAIÚSCULAS E MINÚSCULAS SÃO IGUAIS

texto = input('Texto: ')
distintos = []

for i in range(len(texto)):
    if (texto[i] >= 'a') and (texto[i] <= 'z'):
        s = chr(ord(texto[i]) - 32)
    else:
        s = texto[i]
    if (s not in distintos):
        distintos.append(s)

print('Distintos:', distintos)

