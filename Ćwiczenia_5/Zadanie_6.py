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


z1 = zespolona()
z2 = zespolona()
z1.wczytanie()
z2.wczytanie()
z1.dodawanie(z2).wypisywanie()
z1.odejmowanie(z2).wypisywanie()
z1.mnozenie(z2).wypisywanie()
z1.dzielenie(z2).wypisywanie()
z1.potegowanie(2).wypisywanie()

