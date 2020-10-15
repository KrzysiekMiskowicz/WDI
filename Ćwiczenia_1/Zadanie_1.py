a = 52
b = 12
suma = a+b
while a+b < 10**6:
    print(a+b)
    a, b = a+b, a
    suma += a