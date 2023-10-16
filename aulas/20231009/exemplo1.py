soma = 0

for i in range(10):
    num = int(input('Numero {}: '.format(i)))
    soma = soma + num

media = soma / (i+1)

print('Média = {:.1f}'.format(media))
