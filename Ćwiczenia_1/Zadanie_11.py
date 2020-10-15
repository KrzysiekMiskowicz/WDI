for i in range(2, 10000):
    dana = i
    dzielnik = 2
    suma = 1
    while dzielnik ** 2 <= dana:
        if dana % dzielnik == 0:
            suma += dzielnik
            if dzielnik ** 2 != dana:
                suma += dana // dzielnik
        dzielnik += 1

    dana = suma
    dzielnik = 2
    suma = 1
    while dzielnik ** 2 <= dana:
        if dana % dzielnik == 0:
            suma += dzielnik
            if dzielnik ** 2 != dana:
                suma += dana // dzielnik
        dzielnik += 1
    if suma == i and dana != i:
        print(i, "i", dana, "to liczby zaprzyjaźnione")