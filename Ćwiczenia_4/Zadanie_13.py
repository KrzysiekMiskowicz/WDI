import random
MAX = 3

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


def find_complementary_numbers(t):
    is_complementary = [[False for _ in range(MAX)] for _ in range(MAX)]
    for i in range(MAX):
        for j in range(MAX):
            a = i
            for b in range(j+1, MAX):
                print("[", i, ",", j, "]\t[", a, ",", b, "]")
                if is_prime(t[i][j] + t[a][b]):
                    is_complementary[i][j] = is_complementary[a][b] = True
            for a in range(i+1, MAX):
                for b in range(0, MAX):
                    print("[", i, ",", j, "]\t[", a, ",", b, "]")
                    if is_prime(t[i][j]+t[a][b]):
                        is_complementary[i][j] = is_complementary[a][b] = True

    complementary_numbers = []
    for i in range(MAX):
        for j in range(MAX):
            if is_complementary[i][j]:
                complementary_numbers.append(t[i][j])
            else:
                complementary_numbers.append(0)

    return complementary_numbers



t = [[random.randrange(1, 50) for j in range(MAX)] for i in range(MAX)]
for i in t:
    print(i)

result = find_complementary_numbers(t)
for i in range(MAX*MAX):
    if i % MAX == 0:
        print()
    print(result[i], end=" ")

