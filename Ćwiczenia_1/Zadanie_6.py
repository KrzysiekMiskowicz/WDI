a = 1
b = 2
dana = 2000
while b**b <= dana:
    b += 1
e = 0.001
x = (a+b)/2

while abs(x**x - dana) > e:
    if x**x > dana:
        b = x
    else:
        a = x
    x = (a+b)/2
print(x)