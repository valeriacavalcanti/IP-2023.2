def quantidade_cidades_por_codigo_UF(lista, codigo_uf):
    qt = 0
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[1]) == codigo_uf):
            qt += 1
    return qt

def quantidade_cidades_por_sigla_UF(lista, sigla_uf):
    qt = 0
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (dados[2] == sigla_uf):
            qt += 1
    return qt

def nome_cidade(lista, codigo):
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[0]) == codigo):
            return dados[3]
    return "Código inválido"

def mesorregioes(lista, uf):
    meso = []
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (dados[2] == uf):
            if (dados[4] not in meso):
                meso.append(dados[4])
    return meso

def populacao(lista, codigo):
    soma = 0
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[1]) == codigo):
            soma += int(dados[17])
    return soma

def latitude(lista, codigo):
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[0]) == codigo):
            return dados[13]
    return -1

def longitude(lista, codigo):
    for i in range(len(lista)):
        dados = lista[i].split(';')
        if (int(dados[0]) == codigo):
            return dados[12]
    return -1
