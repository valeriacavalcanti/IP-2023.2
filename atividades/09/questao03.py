"""
“Uma palavra A é um anagrama de outra palavra B se podemos transformar a palavra A na palavra B apenas trocando de
posição as letras da palavra A. Por exemplo, iracema é um anagrama de america, e estudo é um anagrama de duetos”
[OBI 2023].

Escreva um programa para ler duas palavras e informar se formam um anagrama.

"""

palavra1 = input("Palavra 1: ")
palavra2 = input("Palavra 2: ")

texto1 = palavra1.upper()
texto2 = palavra2.upper()

# parte da hipótese que as palavras são anagrama
anagrama = True

# se tiverem o mesmo tamanho
if (len(texto1) == len(texto2)):
    # se todos os símbolos de texto 1 estão em texto2
    for i in range(len(texto1)):
        if (texto1[i] not in texto2):
            anagrama = False
            break
else:
    anagrama = False

if (anagrama == True):
    print("Anagrama")
else:
    print("Não é.")
