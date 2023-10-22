numeros = [0]*8

for i in range(8):
    numeros[i] = int(input("Número: "))

print("Todos os números - por linha")
for i in range(7, -1,-1):
    print(i, numeros[i])
