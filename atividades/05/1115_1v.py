x, y = input().split()
x, y = int(x), int(y)

while(x != 0) and (y != 0):
    if (x > 0):
        if (y > 0):
            print("primeiro")
        else:
            print("quarto")
    else:
        if (y > 0):
            print("segundo")
        else:
            print("terceiro")

    x, y = input().split()
    x, y = int(x), int(y)w
