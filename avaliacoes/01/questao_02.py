avaliacoes = int(input('Quantidade: '))

qt = soma = 0

for i in range(avaliacoes):
    nota = int(input('Nota: '))
    if (nota >= 70) and (nota < 90):
        qt += 1
        soma += nota

media = soma / qt
print("{:.2f}".format(media))

