lista = [12,5,78,40,30,60]
outro = int(input("Valor: "))

if (outro in lista):
    print('existe no índice', lista.index(outro))
else:
    print('nao existe')
