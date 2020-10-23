import math
'''
def zad5(num: int):
    ans = 0
    mask: int = 1
    # while mask <= num:

    for mask in range(1, 1<<(int(math.log10(num))+1)):
        print(bin(mask))
        single_bit = 1
        tmp_num = num
        pow10 = 1
        generated_num = 0
        while tmp_num:
            if single_bit & mask:
                generated_num += pow10*(tmp_num % 10)
                pow10 *= 10

            tmp_num //= 10
            single_bit *= 2  # bit<<1

        if generated_num % 7 == 0:
            ans += 1
            print(generated_num)

        mask += 1

    return ans

num = 1283
ans = 0
mask: int = 1
# while mask <= num:
for mask in range(1, 1 << (int(math.log10(num)) + 1)):
    print(bin(mask))
'''
liczba = 2315
wynik = 0
maska = 1
while maska in range(1, 1 << int(math.log10(liczba) + 1)):
    bit_przesuwny = 1
    waga_bitu = 1
    pom_liczba = liczba
    generowana_liczba = 0
    while pom_liczba:
        if bit_przesuwny & maska:
            generowana_liczba += waga_bitu * (pom_liczba % 10)
            waga_bitu *= 10
        pom_liczba //= 10
        bit_przesuwny *= 2

    if generowana_liczba % 7 == 0 and generowana_liczba > 0:
        wynik += 1
        print(generowana_liczba)
    maska += 1

print(wynik)



