liczba = int(input("Podaj liczbę "))
odp_10 = True
licznik_cyfr = 0
while 10 ** licznik_cyfr <= liczba:
    licznik_cyfr += 1

licznik_cyfr -= 1
waga_cyfr = 0
while licznik_cyfr > waga_cyfr:
    if int(liczba / 10 ** licznik_cyfr) % 10 == int(liczba / 10 ** waga_cyfr) % 10:
        licznik_cyfr -= 1
        waga_cyfr += 1
    else:
        odp_10 = False
        break

odp_2 = True
licznik_bitow = 0
while 2 ** licznik_bitow <= liczba:
    licznik_bitow += 1

licznik_bitow -= 1
waga_bitow = 0
while licznik_bitow > waga_bitow:
    if int(liczba / 2 ** licznik_bitow) % 2 == int(liczba / 2 ** waga_bitow) % 2:
        licznik_bitow -= 1
        waga_bitow += 1
    else:
        odp_2 = False
        break

print("Palindrom w systemie 10:", odp_10)
print("Palindrom w systemie 2:", odp_2)

