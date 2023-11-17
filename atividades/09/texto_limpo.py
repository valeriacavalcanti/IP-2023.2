texto = input('Texto: ')
texto_limpo = ''
tam = len(texto)
i=0
while (i < tam):
    # teste para ignorar os espaços em branco no inicio do texto
    if (texto[i]==' ') and (i==0):
        while (texto[i] == ' '):
            i += 1
    elif (texto[i] == ' ') :
        # teste para ignorar os espacos em branco entre palavras
        while ((i+1) < tam) and (texto[i+1] == ' '):
            i += 1
        # teste para ignorar o espaco em branco no final do texto
        if ((i+1) == tam):
            break
    texto_limpo += texto[i]
    i += 1

print(texto_limpo)
        
