alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nao_utilizadas = []
original = input("Informe o texto: ")
texto = original.upper()

for i in range(len(alfabeto)):
    if (alfabeto[i] not in texto):
        nao_utilizadas.append(alfabeto[i])

print(nao_utilizadas)
