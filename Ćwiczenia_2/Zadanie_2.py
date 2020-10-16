liczba = int(input("Podaj liczbę "))
odp = False
if liczba <= 5:
    pass
else:
    n = 1
    An = 0
    while An <= liczba / 2:
        An = n * n + n + 1
        if liczba % An == 0 and liczba != An:
            odp = True
            break
        n += 1

print(odp)