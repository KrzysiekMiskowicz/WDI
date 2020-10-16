#liczba = int(input("Wprowadź liczbę "))
for i in range(0, 100):
    liczba = i
    a0 = 1
    a1 = 1
    suma = 1
    while suma <= liczba:
        suma += a1
        a0, a1 = a1, a0+a1

    a0 = 1
    a1 = 1
    while True:
        if suma-a0 > liczba:
            suma -= a0
            a0, a1 = a1, a0+a1
        else:
            break

    print(suma)