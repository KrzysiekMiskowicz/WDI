for iterator in range(1, 20):
    dana = iterator
    wynik = True
    i = 2
    while i**2 <= dana:
        if dana % i == 0:
            wynik = False
            break
        i += 1
    if wynik:
        print(iterator, "+")
    else:
        print(iterator, "-")
