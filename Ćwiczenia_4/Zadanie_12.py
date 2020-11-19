import random
MAX = 4

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n < 2:
        return False

    divider = 5
    while divider*divider <= n:
        if n % divider == 0 or n % (divider+2) == 0:
            return False
        divider += 6

    return True


def is_k_composit_numbers_in_every_lines(t, k):
    for i in range(MAX):
        counter = 0
        for j in range(MAX):
            if not is_prime(t[i][j]):
                counter += 1

        if counter < k:
            return False

    return True

t = [[random.randrange(1, 100) for j in range(MAX)] for i in range(MAX)]
for i in t:
    print(i)
print(is_k_composit_numbers_in_every_lines(t, 3))
