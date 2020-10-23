a0 = 0
a1 = 1
b0 = 2
an = 0
bn = 0
# an = an-1 - bn-1 * an-2
# bn = bn-1 + 2 * an-1
# an -> 0, 2
# bn -> 2, 2
print("an = an-1 - bn-1 * an-2\nbn = bn-1 + 2 * an-1")

while True:
    number = int(input("Podaj kolejną liczbę ciągu An -> "))
    if an == 0:
        bn = b0 + 2*a0
        an, bn = a1 - bn*a0, bn + 2*an
    else:
        an, bn, a1 = an - bn*a1, bn * 2*an, an

    if number == an:
        print(bn)
    else:
        break
