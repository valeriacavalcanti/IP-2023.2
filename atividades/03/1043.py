l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

"""
  Lembre que, se o salário for R$ 3002.00, 
  a taxa que incide é de 8% apenas sobre R$ 1000.00, 
  pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. 
  No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, 
  o que resulta em R$ 80.36 no total. 
"""

if (l1 > l2) and (l1 > l3):
  maior = l1
  soma = l2 + l3
else:
  if (l2 > l3):
    maior = l2
    soma = l1 + l3
  else:
    maior = l3
    soma = l1 + l2

if (soma > maior):
  perimetro = l1 + l2 + l3
  print('Perimetro = {:.1f}'.format(perimetro))
else:
  area = ((l1 + l2) * l3) / 2
  print('Area = {:.1f}'.format(area))
