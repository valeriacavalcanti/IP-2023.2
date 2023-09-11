tempo = int(input("Tempo: "))
velocidade = int(input("Velocidade: "))

# velocidade = distancia/tempo
distancia = velocidade * tempo

# autonomia = distancia/combustivel
combustivel = distancia / 12

print("{:.3f}".format(combustivel))
