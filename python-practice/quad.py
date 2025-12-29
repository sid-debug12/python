a = input("Enter the value of a in the quadratic equation : ")
a = int(a)

b = input("Enter the value of b in the quadratic equation : ")
b = int(b)

c = input("Enter the value of c in the quadratic equation : ")
c = int(c)

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solution")
        else:
            print("Absurde")
    else:
        print("First degree quadratic equation")
        x = -c / b
        print(f"{x}")
else:
    D = b * b - 4 * a * c
    D = float(D)

if D == 0:
    x0 = -b / 2 * a
    print(f"Double solution {x0}")

elif D > 0:
    x1 = (-b - D ** 1/2) / 2 * a
    x2 = (-b + D ** 1/2) / 2 * a
    print(f"The solutions are {x1} and {x2}")

else:
    print("Complex solution")
