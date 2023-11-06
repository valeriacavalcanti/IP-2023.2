nome = input('Nome: ')

# exibir com símbolos do alfabeto minúsculo

for i in range(len(nome)):
    if (nome[i] >= 'A') and (nome[i] <= 'Z'):
        codigo = ord(nome[i]) + 32
        print(nome[i], chr(codigo))
    else:
        print(nome[i], nome[i])
