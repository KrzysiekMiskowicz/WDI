szukana = 14
wynik = False
a = 1
b = 1
if szukana == a:
    wynik = True
else:
    while a+b <= szukana:
        if a+b == szukana:
            wynik = True
            break
        else:
            a, b = a+b, a
if wynik:
    print("Tak")
else:
    print("Nie")