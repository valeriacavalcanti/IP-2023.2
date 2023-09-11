salario = float(input("Salário: "))

"""
  Lembre que, se o salário for R$ 3002.00, 
  a taxa que incide é de 8% apenas sobre R$ 1000.00, 
  pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. 
  No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, 
  o que resulta em R$ 80.36 no total. 
"""

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
