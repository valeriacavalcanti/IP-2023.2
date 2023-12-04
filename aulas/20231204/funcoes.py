# lista: lista contendo todos os registros
# uf: código da UF
def quantidade_cidade_codigo_UF(lista, uf):
    qtd = 0
    for i in range(len(lista)):
        dados = lista[i].split(',')
        if (int(dados[1]) == uf):
            #print(dados)
            qtd += 1
    return qtd


# lista: lista contendo todos os registros
# uf: sigla da UF
def quantidade_cidade_sigla_UF(lista, uf):
    qtd = 0
    for i in range(len(lista)):
        dados = lista[i].split(',')
        if (dados[2] == uf.upper()):
            qtd += 1
    return qtd


def cidade(lista, cod_cidade):
    for i in range(len(lista)):
        # separando os campos de cada municipio
        dados = lista[i].split(',')
        if (int(dados[0]) == cod_cidade):
            return dados[3]
    return "código inexistente"




            
