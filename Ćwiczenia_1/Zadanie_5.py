n = 5
k = 3
if n < k:
    newton = 0
else:
    licznik = 1
    mianownik = 1
    for i in range(2, n+1):
        licznik *= i
        if i <= k:
            mianownik *= i
        if i <= n-k:
            mianownik *= i
    newton = licznik // mianownik

A = newton
a = A/2
e = 0.001
while abs(A/a - a) >= e:
    a = (A/a+a)/2
print(newton)
print(a)
