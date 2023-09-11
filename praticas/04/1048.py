salario_inicial = float(input("Salário: "))

if (salario_inicial <= 400):
    aliquota = 15
elif (salario_inicial > 400) and (salario_inicial <= 800):
    aliquota = 12
elif (salario_inicial > 800) and (salario_inicial <= 1200):
    aliquota = 10
elif (salario_inicial > 1200) and (salario_inicial <= 2000):
    aliquota = 7
else:
    aliquota = 4

reajuste = salario_inicial * (aliquota/100)
salario_final = salario_inicial + reajuste

print('Novo salario: {:.2f}'.format(salario_final))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual:', aliquota, '%')
