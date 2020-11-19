n = 10000000
powtorzenia_5 = 0
wykladnik_potegi = 1
while 5 ** wykladnik_potegi <= n:
    powtorzenia_5 += int(n / 5 ** wykladnik_potegi)
    wykladnik_potegi += 1

ostatnia_cyfra = 1
for i in range(1, n+1):
    while i % 5 == 0:
        i /= 5
    if i % 2 == 0 and powtorzenia_5 > 0:
        i /= 2
        powtorzenia_5 -= 1
    ostatnia_cyfra = (ostatnia_cyfra * (i % 10)) % 10

print(int(ostatnia_cyfra))

