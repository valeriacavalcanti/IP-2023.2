maiusculo = 0
numero = 0
especial = 0

senha = input('Senha: ')

for i in range(len(senha)):
    if (senha[i] >= 'A') and (senha[i] <= 'Z'):
        maiusculo += 1
    elif (senha[i] >= '0') and (senha[i] <= '9'):
        numero += 1
    elif (senha[i] < 'a') or (senha[i] > 'z'):
        especial += 1

# opcao 1
if (len(senha) >= 8) and (maiusculo == 1) and (numero == 3) and (especial == 2):
    print('Senha válida')
else:
    print('Senha inválida')

# opcao 2
if (len(senha) >= 8) and (maiusculo >= 1) and (numero >= 3) and (especial >= 2):
    print('Senha válida')
else:
    print('Senha inválida')
