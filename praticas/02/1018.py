valor = int(input("Valor: "))

valor_inicial = valor

c100 = valor // 100
valor = valor % 100

c50 = valor // 50
valor = valor % 50

c20 = valor // 20
valor = valor % 20

c10 = valor // 10
valor = valor % 10

c5 = valor // 5
valor = valor % 5

c2 = valor // 2
c1 = valor % 2

print(valor_inicial)
print(c100, 'nota(s) de R$ 100,00')
print(c50, 'nota(s) de R$ 50,00')
print(c20, 'nota(s) de R$ 20,00')
print(c10, 'nota(s) de R$ 10,00')
print(c5, 'nota(s) de R$ 5,00')
print(c2, 'nota(s) de R$ 2,00')
print(c1, 'nota(s) de R$ 1,00')
