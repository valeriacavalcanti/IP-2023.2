def total(lista, periodo):
    soma = 0
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[2]) == periodo):
            soma += int(dados[1])
    return soma

def maior(lista):
    maior_ch = -1
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[1]) > maior_ch):
            maior_ch = int(dados[1])
    return maior_ch

def periodos(lista):
    temp = []
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (dados[2] not in temp):
            temp.append(dados[2])
    return len(temp)

def disciplinas(lista, carga_horaria):
    temp = []
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[1]) == carga_horaria):
            temp.append(dados[0])

    return temp
