cores = []
frequencias = []

# definir a matriz para a imagem
imagem = []
for i in range(20):
    imagem.append([0] * 20)

# ler os píxels (cor) da imagem
for i in range(20):
    for j in range(20):
        imagem[i][j] = int(input())

# calcular a frequência das diferentes cores
for i in range(20):
    for j in range(20):
        if (imagem[i][j] not in cores):
            cores.append(imagem[i][j])
            frequencias.append(1)
        else:
            posicao = cores.index(imagem[i][j])
            frequencias[posicao] += 1

# exibir as cores para montar o histograma
for i in range(len(cores)):
    print("cor {}: {}".format(cores[i], frequencias[i]))
