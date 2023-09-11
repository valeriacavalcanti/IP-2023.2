x = float(input("X: "))
y = float(input("Y: "))

if (x == 0) and (y == 0):
    print("Origem")
else:
    if (x == 0) and (y != 0):
        print("Eixo Y")
    else:
        if (x != 0) and (y == 0):
            print("Eixo X")
        else:        
            if (x > 0):
                if (y > 0):
                    print("Q1")
                else:
                    print("Q4")
            else:
                if (y > 0):
                    print("Q2")
                else:
                    print("Q3")
