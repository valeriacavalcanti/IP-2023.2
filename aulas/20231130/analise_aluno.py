arq = open('alunos.csv', 'r', encoding="utf8")

lista = arq.read().splitlines()
for i in range(len(lista)):
    print(lista[i])
    break
print(len(lista))
    
arq.close()
