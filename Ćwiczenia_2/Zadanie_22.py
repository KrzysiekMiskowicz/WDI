'''
a = int(input("Podaj licznik "))
b = int(input("Podaj mianownik "))
c = (a/b)

odp = False
waga_cyfry = 0
while 10 ** waga_cyfry <= c:
    waga_cyfry += 1

print(c)
waga_cyfry -= 1
if waga_cyfry < 0:
    wynik = "0."
rzad_liczby = waga_cyfry
while rzad_liczby < waga_cyfry + 10:
    cyfra = int(c / 10 ** waga_cyfry) % 10
    okres = 1
    while okres <= 6:
        if cyfra == int(c / 10 ** (waga_cyfry - okres)) % 10 and cyfra == int(c / 10 ** (waga_cyfry - 2*okres)) % 10:
            string_okres = "(" + chr(48+cyfra)
            for i in range(1, okres):
                cyfra_okresowa = int(c / 10 ** (waga_cyfry-i)) % 10
                if cyfra_okresowa == int(c / 10 ** (waga_cyfry-i - okres)) % 10 and cyfra_okresowa == int(c / 10 ** (waga_cyfry-i - 2 * okres)) % 10:
                    string_okres += chr(48+cyfra_okresowa)
                    if i == okres-1:
                        string_okres += ")"
                        odp = True
                else:
                    break
            if odp:
                break
        okres += 1
    if odp:
        wynik += string_okres
        break
    wynik += chr(48+cyfra)
    waga_cyfry -= 1

if odp:
    print(wynik)
'''

a = int(input("Podaj licznik "))
b = int(input("Podaj mianownik "))
c = a/b

result = False
T = False
T_string = "("
precision = 15
integer_digits = 0
tmp_division = int(c)
while tmp_division > 0:
    integer_digits += 1
    tmp_division //= 10

print(int(c), end=".")
c -= int(c)
fraction_precision = precision-integer_digits
for i in range(fraction_precision):
    if c % 1 == 0:
        break
    c *= 10
    digit = int(c % 10)
    shift_digits = 0
    shift_digits_power = -1
    while shift_digits_power > -fraction_precision + i:
        shift_digits = int((c // 10 ** shift_digits_power) % 10)
        #print("\t", shift_digits)
        if shift_digits == digit:
            T = True
            T_len = -shift_digits_power
            for j in range(T_len):
                T_string += chr(48+int((c // 10 ** (- j)) % 10))
                counter = 1
                while(- j - T_len*counter -1 > -fraction_precision):
                    if (c // 10 ** (- j - T_len*counter)) % 10 != (c // 10 ** (- j)) % 10:
                        print("iteracja", j, "dl", T_len, "licz", counter, "przesunięcie", (- j - T_len*counter -1), "liczba", (c // 10 ** (- j - T_len*counter -1)) % 10, "stala", (c // 10 ** (- j)) % 10)
                        T = False
                        T_string = "("
                        break
                    counter += 1

                if not T:
                    break

            if T:
                break
        shift_digits_power -= 1

    if T:
        T_string += ")"
        print(T_string)
        break
    print(chr(48 + digit), end="")

print()
print(1/7)
