hi = int(input('Hora Inicial: '))
hf = int(input('Hora Final: '))

if (hi < hf):
  tempo = hf - hi
else:
  tempo = 24 - hi + hf

print("O JOGO DUROU {} HORA(S)".format(tempo))
