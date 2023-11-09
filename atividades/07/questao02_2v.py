texto = input('Texto: ')

novo_texto = ''

for i in range(len(texto)):
    if (texto[i] >= 'a') and (texto[i] <= 'z'):
        codigo = ord(texto[i]) - 32
        novo_texto = novo_texto + chr(codigo)
    else:
        novo_texto = novo_texto + texto[i]

print(texto)
print(novo_texto)
