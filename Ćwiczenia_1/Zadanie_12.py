liczba1 = 12
liczba2 = 16
liczba3 = 24
dzielnik = 1
max_dzielnik = 1
najmniejsza = min(liczba1, liczba2, liczba3)
while dzielnik**2 <= najmniejsza:
    if liczba1 % (najmniejsza / dzielnik) == 0 and liczba2 % (najmniejsza / dzielnik) == 0 and liczba3 % (najmniejsza / dzielnik) == 0:
        max_dzielnik = najmniejsza // dzielnik
        break
    if liczba1 % dzielnik == 0 and liczba2 % dzielnik == 0 and liczba3 % dzielnik == 0:
        max_dzielnik = dzielnik
    dzielnik += 1
print(max_dzielnik)
