arq = open('exemplo.txt', 'r')

lista = arq.read().splitlines()
print(lista)
    
arq.close()
