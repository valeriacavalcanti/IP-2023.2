letra_maiuscula = 0
letra_minuscula = 0
numero = 0
especial = 0
vogal = 0
consoante = 0

texto = input('Digite um texto: ')

for i in range(len(texto)):
    if (texto[i] >= 'A') and (texto[i] <= 'Z'):
        letra_maiuscula += 1
        if (texto[i] in 'AEIOU'):
            vogal += 1
        else:
            consoante += 1
    elif (texto[i] >= 'a') and (texto[i] <= 'z'):
        letra_minuscula += 1
        if (texto[i] in 'aeiou'):
            vogal += 1
        else:
            consoante += 1
    elif (texto[i] >= '0') and (texto[i] <= '9'):
        numero += 1
    else:
        especial += 1

# exibir tudo
print('Letra maiuscula:', letra_maiuscula)
print('Letra minuscula:', letra_minuscula)
print('Numero:', numero)
print('Especial:', especial)
print('Vogal:', vogal)
print('Consoante:',consoante)
