def times(lista):
    nomes = []
    for i in range(len(lista)):
        dados = lista[i].split(';')
        nomes.append(dados[1])
    return nomes


def total_gols(lista):
    soma = 0
    for i in range(len(lista)):
        dados = lista[i].split(';')
        soma += int(dados[7])
    return soma


def media_gols_rodadas(lista):
    return total_gols(lista)/38


def media_gols_jogos(lista):
    return total_gols(lista)/380


def rebaixados(lista):
    nomes = []
    tam = len(lista)
    for i in range(tam-4, tam):
        dados = lista[i].split(';')
        nomes.append(dados[1])
    return nomes

def libertadores(lista):
    nomes = []
    for i in range(6):
        dados = lista[i].split(';')
        nomes.append(dados[1])
    return nomes
    
