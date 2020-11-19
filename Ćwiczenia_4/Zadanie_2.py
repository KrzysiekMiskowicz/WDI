import random

MAX = 3
tab = [[random.randrange(1, 100) for i in range(MAX)] for j in range(MAX)]

for i in tab:
    print(i)

exist = True
for i in range(MAX):
    odd_digits_l = False
    for j in range(MAX):
        odd_digits_n = True
        n = tab[i][j]
        while n > 0:
            if n % 2 == 0:
                odd_digits_n = False
                break
            n //= 10

        if odd_digits_n:
            odd_digits_l = True
            break

    if not odd_digits_l:
        exist = False
        break

print(exist)
