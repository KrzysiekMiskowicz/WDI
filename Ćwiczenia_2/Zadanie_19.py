for a in range(1, 11):
    b = a+1
    c = b+1
    while a**2 + (c-1)**2 >= c**2:
        if a**2 + b**2 == c**2:
            print(a, b, c)
            break
        elif a**2 + b**2 < c**2:
            b += 1
        else:
            c += 1

