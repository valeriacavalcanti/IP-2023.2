l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

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
