from funcoes import *

# QUANTIDADE DE CLIENTES (CONSIDERANDO 4, PARA TESTE)
qt = 4


# LISTAS PARA ARMAZENAR OS DADOS
nomes = [''] * qt
compras = [0] * qt
formas = [0] * qt


# LEITURA DOS DADOS
for i in range(qt):
    nomes[i] = input('Nome: ')
    compras[i] = float(input('Valor da Compra: '))
    formas[i] = int(input('Forma de Pagamento: '))


# VALOR MÉDIO DAS COMPRAS
print('Valor médio das compras:', media(compras))


# MAIOR VALOR VENDIDO
maior_valor_vendido = maior(compras)
print('Maior valor vendido: ', maior_valor_vendido, 'tem: ', cupons(maior_valor_vendido))


# VALOR TOTAL DOS DESCONTOS CONCEDIDOS
soma = 0
for i in range(qt):
    soma += descontos(compras[i], formas[i])
print('Total dos descontos:', soma)


# SENHAS DE TODOS OS CLIENTES
print('Nomes de todos os clientes')
for i in range(qt):
    print(senha(nomes[i]))


# MENOR VALOR ÚNICO
menor_valor_unico = menor(compras)

# QUEM FEZ A COMPRA COM MENOR VALOR ÚNICO
for i in range(qt):
    if (compras[i] == menor_valor_unico):
        print(nomes[i])
        break
