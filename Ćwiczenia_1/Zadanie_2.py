"""
a = 600
b = 100
while a+b <= 2020:
    print(a+b)
    a, b = a+b, a
"""
min_suma = 5000
for a1 in range(1, 1010):
    if a1 > int(min_suma/2):
        break
    for a2 in range(a1+1, 2020):
        if a1+a2 > min_suma:
            break
        suma = a1+a2
        b1 = a1
        b2 = a2
        while b2 <= 2020:
            if b2 == 2020:
                if min_suma > suma:
                    min_suma = suma
                    print("Dla a1=%d \ta2=%d \tsuma=%d" % (a1, a2, suma))
                else:
                    pass
                break
            else:
                b2, b1 = b1+b2, b2
