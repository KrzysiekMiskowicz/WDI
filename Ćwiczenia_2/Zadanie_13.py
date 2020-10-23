a2L = 0
a1L = 0
a0 = 0
a1R = 0
a2R = 0
anxt = 0
licznik = 0
zero = False
while True:
    if licznik == 0:
        a2L = int(input("Wpisz liczbę "))
    elif licznik == 1:
        a1L = int(input("Wpisz liczbę "))
    elif licznik == 2:
        a0 = int(input("Wpisz liczbę "))
    elif licznik == 3:
        a1R = int(input("Wpisz liczbę "))
    elif licznik == 4:
        a2R = int(input("Wpisz liczbę "))
    else:
        anxt = int(input("Wpisz liczbę "))
        if anxt == 0:
            zero = True
    if licznik == 4:
        if a2L == (a0+a1L+a1R+a2R)/4:
            print(a2L)
        if a1L == (a0+a2L+a1R+a2R)/4:
            print(a1L)
    elif licznik > 4:
        if a0 == (a2L+a1L+a1R+a2R)/4:
            print(a0)
        if zero:
            if a1R == (a2L+a1L+a0+a2R)/4:
                print(a2L)
            if a2R == (a2L+a1L+a0+a1R)/4:
                print(a1L)
            break
        else:
            a2L, a1L, a0, a1R, a2R = a1L, a0, a1R, a2R, anxt
    licznik += 1

