class ulamek:
    def __init__(self, l = 1, m = 1):
        self.l = l
        self.m = m

    def wczytanie(self):
        l = int(input("Podaj licznik -> "))
        m = int(input("Podaj mianownik -> "))
        self. l = l
        self.m = m

    def wypisywanie(self):
        print("(", self.l, "/", self.m, ")")

    def skracanie(self):
        nwd = NWD(self.l, self.m)
        self.l //= nwd
        self.m //= nwd

    def dodawanie(self, skladnik):
        nww = NWW(self.m, skladnik.m)
        suma = ulamek(int(self.l*(nww/self.m)+skladnik.l*(nww/skladnik.m)), nww)
        suma.skracanie()
        return suma

    def odejmowanie(self, odjemnik):
        nww = NWW(self.m, odjemnik.m)
        roznica = ulamek(int(self.l*(nww/self.m)-odjemnik.l*(nww/odjemnik.m)), nww)
        roznica.skracanie()
        return roznica

    def mnozenie(self, czynnik):
        iloczyn = ulamek(self.l*czynnik.l, self.m*czynnik.m)
        iloczyn.skracanie()
        return iloczyn

    def dzielenie(self, dzielnik):
        iloraz = ulamek(self.l*dzielnik.m, self.m*dzielnik.l)
        iloraz.skracanie()
        return iloraz

    def potegowanie(self, wykladnik):
        wynik = ulamek()
        for i in range(wykladnik):
            wynik = wynik.mnozenie(self)

        return wynik

def NWW(n1, n2):
    nww = 1
    while n1 % 2 == 0 and n2 % 2 == 0:
        nww *= 2
        n1 //= 2
        n2 //= 2

    dzielnik = 3
    while n1 >= dzielnik and n2 >= dzielnik:
        if n1 % dzielnik == 0 and n2 % dzielnik == 0:
            n1 //= dzielnik
            n2 //= dzielnik
            nww *= dzielnik
            continue
        dzielnik += 2

    nww = nww * n1 * n2
    return nww

def NWD(n1, n2):
    nwd = 1
    while n1 % 2 == 0 and n2 % 2 == 0:
        n1 //= 2
        n2 //= 2
        nwd *= 2

    dzielnik = 3
    while n1 >= dzielnik and n2 >= dzielnik:
        if n1 % dzielnik == 0 and n2 % dzielnik == 0:
            n1 //= dzielnik
            n2 //= dzielnik
            nwd *= dzielnik
            continue
        dzielnik += 2

    return nwd

def rozwiazanie(a1, b1, c1, a2, b2, c2):
    # a1*x + b1*y = c1 -> x = (c1 - b1*y)/a1
    # a2*x + b2*y = c2
    w = a1*b2 - a2*b1
    wx = c1*b2 - c2*b1
    wy = a1*c2 - a2*c1
    if w == 0:
        if wx == 0 and wy == 0:
            print("Układ nieoznaczony")
        else:
            print("Układ sprzeczny")
    else:
        x = ulamek(wx, w)
        x.skracanie()
        y = ulamek(wy, w)
        y.skracanie()
        x.wypisywanie()
        y.wypisywanie()
        
rozwiazanie(1, 1, 2, 1, 2, 3)
