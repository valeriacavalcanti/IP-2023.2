while (True):
    m, n = input().split()
    m, n = int(m), int(n)

    if (m <= 0) or (n <= 0):
        break;

    if (m < n):
        m,n = n, m

    soma = 0
    for i in range(n, m + 1):
        print(i, end = " ")
        soma += i

    print("Sum={}".format(soma))
