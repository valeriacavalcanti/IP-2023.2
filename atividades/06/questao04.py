matriz = []
for i in range(20):
    matriz.append([0] * 3)

for i in range(20):
    print("Aluno: ", i + 1)
    for j in range(3):
        matriz[i][j] = int(input("Nota {}: ".format( j + 1)))

for i in range(20):
    print("Aluno:", i + 1, "- notas:", matriz[i])
