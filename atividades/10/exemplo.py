import funcoes
#from funcoes import *

# programa principal

numeros = [0] * 4
for i in range(len(numeros)):
    numeros[i] = int(input("Valor: "))

funcoes.exibir(numeros)
print(funcoes.maior(numeros))
print(funcoes.menor(numeros))
print(funcoes.diferentes(numeros))



