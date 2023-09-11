salario = float(input("Salário: "))

if (salario <= 2000):
    ir = 0                          # faixa 01
elif (salario <= 3000):
    ir = 0                          # faixa 01
    ir += (salario - 2000) * 0.08   # faixa 02
elif (salario <= 4500):
    ir = 0                          # faixa 01
    ir += 1000 * 0.08               # faixa 02
    ir += (salario - 3000) * 0.18   # faixa 03
else:
    ir = 0                          # faixa 01
    ir += 1000 * 0.08               # faixa 02
    ir += 1500 * 0.18               # faixa 03
    ir += (salario - 4500) * 0.28   # faixa 04

if (ir == 0):
    print('Isento')
else:
    print('R$ {:.2f}'.format(ir))
