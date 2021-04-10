def waga(n):
    if n < 2:
        return 0
    dzielniki_pierwsze = 0
    dzielnik = 2
    while n != 1:
        if n % dzielnik == 0:
            dzielniki_pierwsze += 1
            while n % dzielnik == 0:
                n //= dzielnik
        dzielnik += 1

    return dzielniki_pierwsze

def podzbiory(dzielniki, n, s1, s2, s3):
    if len(dzielniki) == n:
        if s1 == s2 == s3:
            return True
        else:
            return False

    return podzbiory(dzielniki, n+1, s1+waga(dzielniki[n]), s2, s3)\
           or podzbiory(dzielniki, n+1, s1, s2+waga(dzielniki[n]), s3)\
           or podzbiory(dzielniki, n+1, s1, s2, s3+waga(dzielniki[n]))


def f(dzielniki):
    suma = 0
    for i in dzielniki:
        suma += waga(i)

    if suma % 3 != 0:
        return False

    return podzbiory(dzielniki, 0, 0, 0, 0)

t = [30, 15, 4, 2, 14]
print(f(t))

#można użyc slisgu tablicy -> tab[1:]