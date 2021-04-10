#dzielniki liczby inne niż ona sama
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
