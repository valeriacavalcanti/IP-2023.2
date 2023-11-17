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
          if (texto1.count(texto1[i]) != texto2.count(texto1[i])):
            anagrama = False
            break       
else:
    anagrama = False

if (anagrama == True):
    print("Anagrama")
else:
    print("Não é.")