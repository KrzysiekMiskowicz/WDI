dana = 1
suma = 0
mianownik = 1
for i in range(10):
    if i == 0:
        pass
    else:
        mianownik *= i
    if i % 4 == 0:
        licznik = dana**i
        suma += licznik / mianownik
    elif i % 4 == 2:
        licznik = dana**i
        suma -= licznik / mianownik
    else:
        pass
print(suma)
