valor = float(input("Valor: "))

if (valor < 0) or (valor > 100):
  print('Fora de intervalo')
else:
    if (valor <= 25):
        print('Intervalo [0,25]')
    else:
        if (valor <= 50):
            print('Intervalo (25,50]')
        else:
            if (valor <= 75):
                print('Intervalo (50,75]')
            else:
                print('Intervalo (75,100]')
