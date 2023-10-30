coluna = int(input())
operacao = input()
soma = 0

matriz = []
for i in range(12):
    matriz.append([0] * 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for i in range(12):
    soma += matriz[i][coluna]

if (operacao == 'S'):
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/12))
