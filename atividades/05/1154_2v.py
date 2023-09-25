soma = qtde = 0

while (True):
    idade = int(input())
    if (idade < 0):
        break

    soma += idade
    qtde += 1

media = soma / qtde

print("{:.2f}".format(media))
