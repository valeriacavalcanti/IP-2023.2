lista = [12,5,78,40,30,60]
outro = int(input("Valor: "))

posicao = -1
for i in range(len(lista)):
    if (lista[i] == outro):
        posicao = i
        break
    
if (posicao == -1):
    print("nao tem")
else:
    print("tem no índice", posicao)
