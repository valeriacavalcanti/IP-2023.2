while (True):
    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)

    if (n1 < n2):
        print("Crescente")
    elif (n1 > n2):
        print("Decrescente")
    else:
        break
