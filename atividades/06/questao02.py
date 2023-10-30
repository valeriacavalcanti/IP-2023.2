matriz = []
for i in range(2):
    matriz.append([0] * 5)

soma = 0
for i in range(2):
    for j in range(5):
        matriz[i][j] = int(input("Valor: "))
        soma = soma + matriz[i][j]

print(soma)
