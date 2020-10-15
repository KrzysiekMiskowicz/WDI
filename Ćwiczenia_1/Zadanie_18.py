n = 6
k = 2
if n > k:
    licznik = 1
    mianownik = 1
    for i in range(2, n+1):
        licznik *= i
        if i <= k:
            mianownik *= i
        if i <= n-k:
            mianownik *= i
    newton = licznik // mianownik
else:
    newton = 0
a = 1
b = 1
while b**3 < newton:
    b += 1
x = (a+b)/2
e = 0.0005
print(newton)
while abs(x**3 - newton) > e:
    if x**3 > newton:
        b = x
    else:
        a = x
    x = (a+b)/2
print(x)
