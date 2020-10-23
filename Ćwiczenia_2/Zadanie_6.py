'''
def zagiezdzenie(liczba, ciag, rzad_cyfry):
    wynik = 0
    if rzad_cyfry == 0:
        if ciag % 7 == 0 and ciag != 0:
            print(ciag)
            wynik += 1
        if (10 * ciag + (liczba % 10)) % 7 == 0:
            print(10 * ciag + (liczba % 10))
            wynik += 1
    elif rzad_cyfry > 0:
        wynik += zagiezdzenie(liczba, ciag, rzad_cyfry-1)
        wynik += zagiezdzenie(liczba, 10 * ciag + ((liczba // 10 ** rzad_cyfry) % 10), rzad_cyfry-1)

    return wynik

print(zagiezdzenie(2315, 0, 3))
print(bin(17))
'''

number = int(input("Wpisz liczbe -> "))

result = 0
temp_number = number
digit_number = 0
while temp_number > 0:
    digit_number += 1
    temp_number //= 10

temp_number = number
mask = 0
for mask in range(1, 2**digit_number):
    digit_value = 1
    shift_bit = 1
    gen_number = 0
    temp_number = number
    while temp_number > 0:
        if shift_bit & mask:
            gen_number += digit_value*(temp_number % 10)
            digit_value *= 10
        shift_bit = shift_bit << 1
        temp_number //= 10

    if gen_number % 7 == 0 and gen_number != 0:
        result += 1
        print(gen_number)

print(result)



