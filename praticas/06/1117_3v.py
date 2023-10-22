soma = 0

while (True):
    nota = float(input())
    if (nota >= 0) and (nota <= 10):
        break
    print('nota invalida')
soma += nota

while (True):
    nota = float(input())
    if (nota >= 0) and (nota <= 10):
        break
    print('nota invalida')
soma += nota

print('media = {:.2f}'.format(soma/2))
