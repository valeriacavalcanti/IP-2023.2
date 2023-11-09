qt = 0

for i in range(10):
    num = input('Digite um número: ')
    valido = True
    for i in range(len(num)):
        if (num[i] < '0') or (num[i] > '9'):
            valido = False
            break
    if (valido == False) or (len(num) == 0):
        qt = qt + 1

print('Quantidade de números inválidos:', qt)
