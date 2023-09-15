num = int(input("N: "))

for i in range(1, num + 1):
    if (i % 2 == 0):
        print('{}^2 = {}'.format(i, i ** 2))
