d1 = input('Dica1: ')
d2 = input('Dica2: ')
d3 = input('Dica3: ')

if (d1 == 'vertebrado'):
  if (d2 == 'ave'):
    if (d3 == 'carnivoro'):
      print('aguia')
    else:
      print('pomba')
  else:
    #sou mamifero
    if (d3 == 'onivoro'):
      print('homem')
    else:
      print('vaca')
else:
  # sou invertebrado
  if (d2 == 'inseto'):
    if (d3 == 'hematofago'):
      print('pulga')
    else:
      print('lagarta')
  else:
    # sou anelideo
    if (d3 == 'hematofago'):
      print('sanguessuga')
    else:
      print('minhoca')
