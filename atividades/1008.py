codigo = int(input("Número: "))
qtde = int(input("Quantidade de horas: "))
valor = float(input("Valor da hora trabalhada: "))

salario = qtde * valor

print('NUMBER =', codigo)
print('SALARY = U$ {:.2f}'.format(salario))