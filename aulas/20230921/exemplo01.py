import random

num = int(input('Valor: '))
secreto = random.randint(1, 100)

while (num != secreto):
    #print("Tá errado")
    if (num > secreto):
        print('Seu número é maior')
    else:
        print('Seu número é menor')
        
    num = int(input('Valor: '))

print('acertou')
