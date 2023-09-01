nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))

media = (nota1 + nota2)/2

print('Média = {:.2f}'.format(media))

if (media >= 70):
    print('aprovado')
else:
    if (media >= 40):
        print('final')
    else:
        print('reprovado')
    
