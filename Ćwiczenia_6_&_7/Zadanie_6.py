def primary_parts(t, n):
    MAX = 30
    if n == len(t):
        return True

    s = 0
    l = min(MAX, len(t) - n - 1)
    for i in range(l+1):
        s = s*2 + t[n+i]
        if is_prime(s) and primary_parts(t, n+i+1):
            print(s, end=" ")
            return True

    return False


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    divider = 5
    while divider*divider <= n:
        if n % divider == 0 or n % (divider + 2) == 0:
            return False
        divider += 6

    return True



t = [1, 1, 1, 0, 1, 1]
print(primary_parts(t, 0))

