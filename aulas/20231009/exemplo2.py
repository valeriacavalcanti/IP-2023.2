soma = 0
numeros = [0] * 6

# percorrer o vetor - armazenar os números
for i in range(len(numeros)):
    numeros[i] = int(input('Numero {}: '.format(i)))
    soma = soma + numeros[i]

media = soma / len(numeros)

print(i)
print(soma)
print(numeros)
print(media)

# percorrer o vetor - exibir os números
for i in range(len(numeros)):
    if (numeros[i] > media):
        print(numeros[i])
