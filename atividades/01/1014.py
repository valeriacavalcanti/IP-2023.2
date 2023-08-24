distancia = int(input("Distância: "))
combustivel = float(input("Quantidade de combustível: "))

consumo = distancia / combustivel

print('{:.3f} km/l'.format(consumo))