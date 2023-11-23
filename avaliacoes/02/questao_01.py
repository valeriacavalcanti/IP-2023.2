temperaturas = [0] * 50
maior = 0
soma = 0
ano = 0

for i in range(50):
    temperaturas[i] = int(input())
    soma += temperaturas[i]
    if (temperaturas[i] > maior):
        maior = temperaturas[i]
        ano = i

# calcular a média geral
media = soma/50
print('Média nos últimos 50 anos:', media)

# calcular a quantidade de anos em que a média anual superou a média geral
qt = 0
for i in range(50):
    if (temperaturas[i] > media):
        qt += 1
print(qt, 'anos superaram a média.')

# maior temperatura regisrada
print('Ano {} registrou a maior temperatura ({})'.format(ano, maior))
