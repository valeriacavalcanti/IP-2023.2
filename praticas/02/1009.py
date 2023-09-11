nome = input("Nome: ")
salario_fixo = float(input("Salário: "))
vendas = float(input("Vendas: "))

salario_final = salario_fixo + (vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(salario_final))
