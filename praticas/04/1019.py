tempo = int(input("Tempo em segundos: "))

horas = tempo // 3600
tempo = tempo % 3600

minutos = tempo // 60
tempo = tempo % 60

segundos = tempo

print(horas, minutos, segundos, sep=':')
