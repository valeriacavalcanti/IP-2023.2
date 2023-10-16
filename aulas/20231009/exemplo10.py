frase = "hoje o dia está lindo"

palavras = frase.split()

final = [" "] * (len(palavras) * 2 - 1)

for i in range(len(palavras)):
    final[i*2] = palavras[i]
