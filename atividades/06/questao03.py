matriz = []
for i in range(3):
    matriz.append([0] * 3)

soma = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Valor: "))

numero = int(input("Pesquisar por: "))

existe = False
for i in range(3):
    for j in range(3):
        if (matriz[i][j] == numero):
            existe = True
            break
    if (existe == True):
        break

if (existe == True):
    print(numero, "existe na matriz", matriz)
else:
    print(numero, "não existe na matriz", matriz)
