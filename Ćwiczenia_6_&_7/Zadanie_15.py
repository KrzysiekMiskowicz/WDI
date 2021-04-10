'''
#działa dla stringów
def wyraz(s1, s2):
    if wartosc_liter(s1) == wartosc_liter(s2):
        if liczba_samoglosek(s1) == liczba_samoglosek(s2):
            print(s2, "+")
            return True
        else:
            return False

    elif wartosc_liter(s1) > wartosc_liter(s2):
        return False

    result = False
    n = len(s2)
    for i in range(n):
        result |= wyraz(s1, s2.replace(s2[i], ""))

    return result
'''
'''
# działa
def wyraz(s1, s2, p, l = 0):
    if wartosc_liter(s1) == wartosc_liter(p):
        if liczba_samoglosek(s1) == liczba_samoglosek(p):
            print(p)
            return True
        else:
            return False

    elif wartosc_liter(s1) < wartosc_liter(p) or l == len(s1):
        #print(s2, "-")
        return False

    return wyraz(s1, s2, p+s2[l], l+1) or wyraz(s1, s2, p, l+1)
'''
#działa dla tablic
def wyraz(s1, s2):
    if wartosc_liter(s1) == wartosc_liter(s2):
        if liczba_samoglosek(s1) == liczba_samoglosek(s2):
            print(s2, "+")
            return True
        else:
            return False

    elif wartosc_liter(s1) > wartosc_liter(s2):
        return False

    result = False
    n = len(s2)
    for i in range(n):
        mem = s2[i]
        s2.remove(s2[i])
        result |= wyraz(s1, s2)
        s2.insert(i, mem)

    return result
def czy_samogloska(s):
    t = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in t:
        if s == i:
            return True

    return False

def liczba_samoglosek(s):
    wynik = 0
    for i in s:
        if czy_samogloska(i):
            wynik += 1

    return wynik

def wartosc_liter(s):
    wynik = 0
    for i in s:
        wynik += ord(i)

    return wynik


s1 = "ula"
s2 = "exeiula"
p = ""
c1 = ['u', 'l', 'a']
c2 = ['e', 'x', 'e', 'i', 'u', 'l', 'a']


#print(wyraz(s1, s2, p))
print(wyraz(c1, c2))