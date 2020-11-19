import random

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

    def porownanie(self, liczba):
        self.skracanie()
        liczba.skracanie()
        return self.l == liczba.l and self.m == liczba.m

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


t = [ulamek() for _ in range(10)]
for i in range(10):
    t[i].wczytanie()
    #t[i] = ulamek(random.randrange(1, 10), random.randrange(1, 10))
    #print("(", t[i].l, "/", t[i].m , ")", end=" ")

print()

def podciagi(t):
    current_a = 2
    max_a = 2
    current_g = 2
    max_g = 2
    for i in range(len(t)-2):
        if t[i].odejmowanie(t[i+1]).porownanie(t[i+1].odejmowanie(t[i+2])):
            current_a += 1
        else:
            max_a = max(max_a, current_a)
            current_a = 2

        if t[i].dzielenie(t[i+1]).porownanie(t[i+1].dzielenie(t[i+2])):
            current_g += 1
        else:
            max_g = max(max_g, current_g)
            current_g = 2

    max_a = max(max_a, current_a)
    max_g = max(max_g, current_g)
    print("max a =", max_a)
    print("max g =", max_g)

    if max_a > max_g:
        return 1
    elif max_a == max_g:
        return 0
    else:
        return -1

print(podciagi(t))

