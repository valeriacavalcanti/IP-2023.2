original = input("Palavra: ")
invertida = ''

# gerar uma nova string com os caracteres "invertidos" da string original
for i in range(len(original) - 1, -1, -1):
    invertida = invertida + original[i]

if (original == invertida):
    print("Palíndromo")
else:
    print("Não é")
