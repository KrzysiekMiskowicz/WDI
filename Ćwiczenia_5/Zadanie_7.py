class zespolona:
    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im

    def wczytanie(self):
        re = float(input("Podaj część realną -> "))
        im = float(input("Podaj część urojoną -> "))
        self.re = re
        self.im = im

    def wypisywanie(self):
        print("(", self.re, ",", self.im, "i)")

    def dodawanie(self, skladnik):
        suma = zespolona(self.re+skladnik.re, self.im+skladnik.im)
        return suma

    def odejmowanie(self, odjemnik):
        roznica = zespolona(self.re-odjemnik.re, self.im-odjemnik.im)
        return roznica

    def mnozenie(self, czynnik):
        iloczyn = zespolona(self.re*czynnik.re - self.im*czynnik.im, self.re*czynnik.im + self.im*czynnik.re)
        return iloczyn

    def dzielenie(self, dzielnik):
        m = dzielnik.re*dzielnik.re+dzielnik.im*dzielnik.im
        iloraz = zespolona((self.re*dzielnik.re + self.im*dzielnik.im) / m, (self.im*dzielnik.re - self.re*dzielnik.im) / m)
        return iloraz

    def potegowanie(self, wykladnik):
        wynik = zespolona(1, 0)
        for i in range(wykladnik):
            wynik = wynik.mnozenie(self)

        return wynik


def rownanie_kwadratowe(a, b, c):
    delta = b*b - 4*a*c
    if delta > 0:
        print("z1 =", ((-1)*b - delta**0.5) / (2*a))
        print("z2 =", ((-1)*b + delta**0.5) / (2*a))
    elif delta == 0:
        print("z1 =", (-1)*b / (2*a))
    else:
        pier_delta = zespolona(abs(delta)**0.5, 1)
        z1 = zespolona((-1)*b).odejmowanie(pier_delta).dzielenie(zespolona(2*a))
        z2 = zespolona((-1)*b).dodawanie(pier_delta).dzielenie(zespolona(2*a))
        z1.wypisywanie()
        z2.wypisywanie()


rownanie_kwadratowe(1, 2, 4)