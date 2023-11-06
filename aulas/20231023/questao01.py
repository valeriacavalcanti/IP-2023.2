TAM = 4

nomes  = [''] * TAM
idades = [0] * TAM


# 1) Ler o nome e a idade de cada integrante do grupo;
for i in range(TAM):
    nomes[i] = input("Nome: ")
    idades[i] = int(input("Idade: "))

#print(nomes)
#print(idades)


# 2) Exibir o nome e a idade de todos os integrantes;
print('Nome e idade de todos os integrantes')
for i in range(TAM):
    print(nomes[i], 'tem', idades[i], 'anos')


# 3) Exibir a média da idade do grupo;
soma = 0
for i in range(TAM):
    soma = soma + idades[i]
media = soma / TAM
print('Media =', media)


# 4) Calcular e exibir quantas pessoas possuem maior idade
#    (idade acima de 17 anos).
qt_maior_idade = 0
for i in range(TAM):
    if (idades[i] >= 18):
        qt_maior_idade = qt_maior_idade + 1
print('Quantidade com maior idade =', qt_maior_idade)


#5) Exibir o nome e a idade de cada integrante que
#   possuir idade acima da média do grupo;
print('Nome e idade de pessoas com idade acima da média')
for i in range(TAM):
    if (idades[i] > media):
        print(nomes[i], idades[i])


# 6) Exibir a menor idade desse grupo;
menor = idades[0]
for i in range(1, TAM):
    if (idades[i] < menor):
        menor = idades[i]
print('Menor idade =', menor)


# 7) Exibir o(s) nome(s) da(s) pessoa(s)
#    que possui(em) a menor idade desse grupo;
print('Pessoas com menor idade do grupo')
for i in range(TAM):
    if (idades[i] == menor):
        print(nomes[i])


# 8) Exibir se existem pessoas com idades iguais.
















