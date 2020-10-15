dana = 16
dzielnik = 1
while dzielnik**2 <= dana:
    if dana % dzielnik == 0:
        print(dzielnik)
        if dzielnik**2 != dana:
            print(dana // dzielnik)
    dzielnik += 1

