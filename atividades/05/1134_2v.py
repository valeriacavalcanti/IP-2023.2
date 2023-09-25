q_alcool = q_gasolina = q_diesel = 0

while (True):
    codigo = int(input())

    if (codigo == 1):
        q_alcool += 1
    elif (codigo == 2):
        q_gasolina += 1
    elif (codigo == 3):
        q_diesel += 1
    elif (codigo == 4):
        break

print("MUITO OBRIGADO")
print("Alcool:", q_alcool)
print("Gasolina:", q_gasolina)
print("Diesel:", q_diesel)
