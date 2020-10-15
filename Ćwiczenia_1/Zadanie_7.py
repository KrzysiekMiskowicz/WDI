for i in range(1, 20):
    dana = i
    wynik = False
    a = 1
    b = 1
    while a + b <= dana:
        if a + b == dana:
            wynik = True
            break
        else:
            a, b = a + b, a
    if wynik:
        print("Tak")
    else:
        print("Nie")
