n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

while (n1 != n2):
    if (n1 < n2):
        print("Crescente")
    else:
        print("Decrescente")

    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)
