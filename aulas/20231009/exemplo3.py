generica = []

generica.append(10)
generica.append(12.2)
generica.append(True)
generica.append([0]*4)

print(type(generica), generica)

for i in range(len(generica)):
    print(i, type(generica[i]), generica[i])
