'''
n1 = int(input("Podaj liczbe -> "))
n2 = int(input("Podaj liczbe -> "))

if n1 < 0:
    n1 *= -1
if n2 < 0:
    n2 *= -1

tmp_n1 = n2
tmp_n2 = n2
n1_zeros = 0
n2_zeros = 0
digit_counter = 0
while 10**digit_counter <= n1 and 10**digit_counter <= n2:
    if (tmp_n1 // 10**digit_counter) % 10 == 0:
        n1_zeros += 1
    if (tmp_n2 // 10**digit_counter) % 10 == 0:
        n2_zeros += 1
    tmp_n1 //= 10
    tmp_n2 //= 10
    digit_counter += 1

if tmp_n1 != 0 or tmp_n2 != 0 or n1_zeros != n2_zeros:
    print(False)
else:
    while n1 > 0:
        digit = n1 % 10
        if digit != 0:
            digit_counter = 0
            repeat = False
            while 10 ** digit_counter <= n2:
                if (n2 // 10 ** digit_counter) % 10 == digit:
                    n2 -= digit * (10 ** digit_counter)
                    repeat = True
                    break
                digit_counter += 1

            if not repeat:
                break
        else:
            pass
        n1 //= 10

    print(n1 == n2)
'''

n1 = int(input("Podaj liczbe -> "))
n2 = int(input("Podaj liczbe -> "))

digits = []
for i in range(10):
    digits.append(0)

while n1 > 0:
    digits[n1 % 10] += 1
    n1 //= 10

while n2 > 0:
    digits[n2 % 10] -= 1
    n2 //= 10

result = True
for i in range(10):
    if digits[i] != 0:
        result = False
        break

print(result)


