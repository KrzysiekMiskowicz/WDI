'''
a = 34
b = 3
n = 100
print(a/b)
wynik = ""
ZERO = 48
kropka = False
dokladniosc = 0
waga_cyfry = 0
while b*10**waga_cyfry <= a:
    waga_cyfry += 1

waga_cyfry -= 1
if waga_cyfry < 0:
    wynik = "0."
    kropka = True
    for i in range(1, (-1)*waga_cyfry):
        dokladniosc += 1
        wynik += "0"

while dokladniosc <= n:
    if waga_cyfry == -1 and kropka == False:
        wynik += "."
        kropka = True
    if waga_cyfry < 0:
        dokladniosc += 1
        a *= 10
        waga_cyfry += 1
    cyfra = a // (b*10**waga_cyfry)
    wynik += chr(ZERO + int(cyfra))
    #print("cyfra =", cyfra, "dzielna =", a, "dzielnik =", (b*10**waga_cyfry))
    a -= cyfra * (b*10**waga_cyfry)
    waga_cyfry -= 1

print(wynik)
#print(0.4285714285714285312704032044404157103010475813947743173575966031775017594849971862405694000315781452*7)
#print(0.02970297029702970297029702970297029702970297029702970297029702970297029702970297029702970297029702970*101)
'''
#algprytm dzielenia pisemnego
a = 34
b = 3
n = 100
print(a//b, end=".")

for i in range(100):
    a %= b
    a *= 10
    print(a//b, end="")
