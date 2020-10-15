mianownik = 1
suma = 0
for i in range(0, 50):
    if i < 2:
        mianownik = 1
    else:
        mianownik *= i
    suma += 1/mianownik
print(suma)