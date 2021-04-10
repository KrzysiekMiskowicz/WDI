def jumps(t, m):
    n = len(t)
    if n == 1:
        return m
    result = -1
    dividers = reversed(prime_dividers(t[0]))
    for i in dividers:
        if i >= n:
            continue
        result = jumps(t[i:], m+1)
        if result != -1:
            break

    return result


def prime_dividers(n):
    if n <= 2:
        return []
    result = []
    temp_n = n
    if temp_n % 2 == 0:
        result.append(2)
        while temp_n % 2 == 0:
            temp_n //= 2

    divider = 3
    while divider <= temp_n:
        if temp_n % divider == 0:
            result.append(divider)
            while temp_n % divider == 0:
                temp_n //= divider

        divider += 2

    if len(result) == 1 and result[0] == n:
        return []
    return result


t = [6, 2, 9, 7, 6]
print(jumps(t, 0))
