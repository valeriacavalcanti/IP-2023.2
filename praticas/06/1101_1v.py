m, n = input().split()
m, n = int(m), int(n)

while (m > 0) and (n > 0):
    if (m < n):
        m,n = n, m

    soma = 0
    for i in range(n, m + 1):
        print(i, end = " ")
        soma += i

    print("Sum={}".format(soma))

    m, n = input().split()
    m, n = int(m), int(n)
