lista = [12,5,78,40,30,60]
outro = int(input("Valor: "))

existe = False
for i in range(len(lista)):
    if (lista[i] == outro):
        existe = True
        break
    
if (existe == False):
    print("nao tem")
else:
    print("tem")
