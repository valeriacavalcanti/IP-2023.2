# declarar a matriz
matriz = []
for i in range(3):
    matriz.append([0] * 3)


# percorrer todos os elementos (índices) da matriz
for i in range(3):
    for j in range(3):
        print(i, j)
    print()

#print(matriz)

# perguntar: linha, coluna e valor
#linha = int(input('Linha: '))
#coluna = int(input('Coluna: '))
#valor = int(input('Valor: '))
#matriz[linha][coluna] = valor

print(matriz)

# exibir todos os elementos da matriz, por linha
#for i in range(3):
#    for j in range(3):
#        print(i, j, matriz[i][j])



for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print()








    
