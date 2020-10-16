#y = 1/x
k = 2
x = 1
dx = 0.0005
calka = 0
while x <= k:
    calka += 1/x*dx
    x += dx

print(calka)
