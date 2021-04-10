def built_binary_number(b, A, B):
    if A == B == 0:
        if not is_prime(b):
            print(b)
            return 1
        else:
            return 0
    if A == 0:
        while B > 0:
            b *= 2
            B -= 1
        return built_binary_number(b, 0, 0)
    elif B == 0:
        while A > 0:
            b = 2*b+1
            A -= 1
        return built_binary_number(b, 0, 0)

    if b == 0:
        return built_binary_number(1, A-1, B)

    counter = 0
    counter += built_binary_number(2*b+1, A-1, B)
    counter += built_binary_number(2*b, A, B-1)
    return counter


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


print(built_binary_number(0, 2, 3))