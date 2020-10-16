liczba = int(input("Podaj liczbę "))
a1 = 1
a2 = 1
odp = False
while a1 * a2 <= liczba:
    if a1 * a2 == liczba:
        odp = True
        break
    a1, a2 = a2, a2 + a1
print(odp)