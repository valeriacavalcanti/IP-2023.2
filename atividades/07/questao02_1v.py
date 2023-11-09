texto = input('Texto: ')

for i in range(len(texto)):
    if (texto[i] >= 'a') and (texto[i] <= 'z'):
        codigo = ord(texto[i]) - 32
        print(chr(codigo), end='')
    else:
        print(texto[i], end='')
