texto = input('Texto: ')
palavras = texto.split()

for i in range(len(palavras) - 1, -1, -1):
    print(palavras[i], end=' ')
