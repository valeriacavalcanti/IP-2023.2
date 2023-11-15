texto = input("Digite um texto: ")

# enquanto encontrar 2 espaços em branco seguidos
while (texto.find('  ') >= 0):
    # troca 2 espaços por 1
    texto = texto.replace('  ', ' ')

# se o primeiro símbolo do texto for espaço em branco, pegar a substring do índice 1 até o final
if (texto[0] == ' '):
    texto = texto[1:]

# se o último símbolo do texto for espaço em branco, pegar até o penúltimo símbolo do texto.
if (texto[len(texto) - 1] == ' '):
    texto = texto[:-1]

print(texto)
