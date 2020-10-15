'''
liczba1 = 12
liczba2 = 16
liczba3 = 24
wszystkie_dzielniki = [[] for i in range(3)]
czynniki_pierwsze_NWW = []
iteracja = 0
for i in liczba1, liczba2, liczba3:
    dzielnik = 2
    while dzielnik <= i:
        if i % dzielnik == 0:
            wszystkie_dzielniki[iteracja].append(dzielnik)
            i /= dzielnik
        else:
            if dzielnik % 2 == 0:
                dzielnik += 1
            else:
                dzielnik += 2
    iteracja += 1
for i in wszystkie_dzielniki[0]:
    if i in wszystkie_dzielniki[1]:
        wszystkie_dzielniki[1].remove(i)
czynniki_pierwsze_NWW = wszystkie_dzielniki[0]+wszystkie_dzielniki[1]
for i in czynniki_pierwsze_NWW:
    if i in wszystkie_dzielniki[2]:
        wszystkie_dzielniki[2].remove(i)
czynniki_pierwsze_NWW += wszystkie_dzielniki[2]
NWW = 1
for i in czynniki_pierwsze_NWW:
    NWW *= i
print(NWW)
'''

liczba1 = 5
liczba2 = 9
liczba3 = 15

dzielnik = 2
NWW = 1
while  dzielnik <= max(liczba1, liczba2, liczba3):
    if liczba1 % dzielnik == 0:
        NWW *= dzielnik
        liczba1 /= dzielnik
        if liczba2 % dzielnik == 0:
            liczba2 /= dzielnik
            if liczba3 % dzielnik == 0:
                liczba3 /= dzielnik
            else:
                pass
        else:
            if liczba3 % dzielnik == 0:
                liczba3 /= dzielnik
            else:
                pass
    elif liczba2 % dzielnik == 0:
        NWW *= dzielnik
        liczba2 /= dzielnik
        if liczba3 % dzielnik == 0:
            liczba3 /= dzielnik
        else:
            pass
    elif liczba3 % dzielnik == 0:
        NWW *= dzielnik
        liczba3 /= dzielnik
    else:
        dzielnik += 1

print(NWW)








