texto = input("Digite um texto: ")

# enquanto encontrar 2 espaços em branco seguidos
while (texto.find('  ') >= 0):
    # troca 2 espaços por 1
    texto = texto.replace('  ', ' ')

# remove os espaços em branco do início e final do texto
texto = texto.strip()

print(texto)
