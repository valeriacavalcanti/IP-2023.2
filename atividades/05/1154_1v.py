soma = qtde = 0

idade = int(input())
while (idade >= 0):
    soma += idade
    qtde += 1
    idade = int(input())

media = soma / qtde

print("{:.2f}".format(media))
