alcool = gasolina = diesel = 0

tipo = int(input())

while (tipo != 4):
    if (tipo == 1):
        alcool = alcool + 1
    elif (tipo == 2):
        gasolina = gasolina + 1
    elif (tipo == 3):
        diesel = diesel + 1

    tipo = int(input())

print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gasolina)
print('Diesel:', diesel)
