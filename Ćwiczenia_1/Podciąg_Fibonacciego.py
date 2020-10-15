#program oblicza sumy podciągów fibonacciego
for i in range(1, 20):
    dana = i
    wynik = False
    suma = 1
    poczatek = 0
    po_poczatku = 1
    koniec = 1
    po_koncu = 1
    while suma <= dana:
        if suma == dana:
            wynik = True
            break
        else:
            if (suma + po_koncu <= dana):
                suma += po_koncu
                po_koncu, koniec = po_koncu + koniec, po_koncu
            else:
                if (po_poczatku > koniec):
                    break
                else:
                    suma -= poczatek
                    po_poczatku, poczatek = po_poczatku + poczatek, po_poczatku
    if wynik:
        print(i, "+")
    else:
        print(i, "-")


