licznik = 0
for i in range(1, 101):
    odp = True
    N = i
    dzielnik = 2
    while dzielnik <= N:
        if N % dzielnik == 0:
            N /= dzielnik
        else:
            if dzielnik < 5:
                dzielnik += 1
            else:
                odp = False
                break
    if odp:
        licznik += 1

print(licznik)