idade = input('Idade: ')

valida = True

for i in range(len(idade)):
    if (idade[i] < '0') or (idade[i] > '9'):
        valida = False
        break

if (valida == False):
    print('Se oriente, você sabe o que é número?')
else:
    idade = int(idade)
    print(idade  * 2)
