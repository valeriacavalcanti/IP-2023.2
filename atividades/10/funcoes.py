#funçoes

def exibir (lista):
    for i in range(len(lista)):
        print(lista[i])

def maior(lista):
    maior_valor = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] > maior_valor):
            maior_valor= lista[i]
    return maior_valor

def menor(lista):
    menor_valor = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] < menor_valor):
            menor_valor= lista[i]
    return menor_valor

def diferentes(lista):
    distintos = []
    for i in range(len(lista)):
        if (lista[i] not in distintos):
            distintos.append(lista[i])
    return distintos
