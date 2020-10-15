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
k = 10
for i in range(k):
    print(i)
    print(k)
    k -= 1