import random

MAX = 5
tab = [[random.randrange(1, 100) for i in range(MAX)] for j in range(MAX)]

for i in tab:
    print(i)

exist = False
for i in range(MAX):
    even_digit_l = True
    for j in range(MAX):
        even_digit_n = False
        n = tab[i][j]
        while n > 0:
            if n % 2 == 0:
                even_digit_n = True
                break
            n //= 10

        if not even_digit_n:
            even_digit_l = False
            break

    if even_digit_l:
        exist = True
        break

print(exist)
