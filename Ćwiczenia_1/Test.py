""" dokładność print/przybliżenia
e = 0.1
for i in range(1, 100):
    X = i
    x = X/2
    while abs(X/x-x) > e:
        x = (X/x+x)/2
    print("Pierwiastek %d = %.2f" % (i, x))

def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    dzielnik = 5
    while dzielnik**2 <= n:
        if n % dzielnik == 0 or n % (dzielnik+2) == 0:
            return False
        dzielnik += 6
    return True

for i in range(1, 100):
    print(i, czy_pierwsza(i))
"""
"""
min_sum = 2020
for a1 in range(1, 1010):
    if a1 == 1:
        a1 += 1

    if 2*a1 > min_sum:
        break

    for a2 in range(a1, 2020):
        current_sum = a1 + a2
        if current_sum > min_sum:
            break

        tmp_a1, tmp_a2 = a1, a2
        while tmp_a2 <= 2020:
            if tmp_a2 == 2020:
                if min_sum > current_sum:
                    min_sum = current_sum
                    print('a1 = {}, a2 = {} -> {}'.format(a1, a2, current_sum))
                    break
            tmp_a1, tmp_a2 = tmp_a2, tmp_a1 + tmp_a2
"""
"""
for i in range(1, 20):
    a1 = 1
    a2 = 1
    sum = a1
    result = False
    while sum <= i:
        if sum == i:
            result = True
            break
        sum += a2
        a1, a2 = a2, a1 + a2

    a1 = 1
    a2 = 1
    while sum >= i:
        if sum == i:
            result = True
            break
        sum -= a1
        a1, a2 = a2, a1 + a2

    print("{} -> {}".format(i, result))
"""

def NWW(n1, n2, n3):
    nww = 1
    dzielnik = 2
    while dzielnik <= max(n1, n2, n3):
        czynnik = False
        if n1 % dzielnik == 0:
            czynnik = True
            n1 //= dzielnik
        if n2 % dzielnik == 0:
            czynnik = True
            n2 //= dzielnik
        if n3 % dzielnik == 0:
            czynnik = True
            n3 //= dzielnik
        if czynnik:
            nww *= dzielnik
            continue
        dzielnik += 1

    return nww

print(NWW(1, 3, 6))






