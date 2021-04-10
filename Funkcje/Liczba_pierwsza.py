def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    divider = 5
    while divider*divider <= n:
        if n % divider == 0 or n % (divider+2) == 0:
            return False
        divider += 6

    return True