lista = [12,5,78,40,30,60]
outro = int(input("Valor: "))

for i in range(len(lista)):
    if (lista[i] == outro):
        break

if (i < len(lista) - 1):
    print('achei no indice', i)
else:
    if (lista[-1] == outro):
        print('achei no último índice')
    else:
        print("nao achei")
