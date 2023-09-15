maior = int(input("Valor: "))
posicao = 1

for i in range(2, 101):
    num = int(input("Valor: "))
    if (num > maior):
        maior = num
        posicao = i

print(maior)
print(posicao)
