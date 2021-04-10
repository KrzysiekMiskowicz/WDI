def found_N_product_it(t, p):
    n = len(t)
    result = 0
    for i in range(1, int(2**n)+1):
        shift_b = 1
        s = 1
        for j in reversed(range(n)):
            if (i & shift_b) != 0:
                s *= t[j]
            shift_b *= 2

        if p == s:
            result += 1

    return result


def found_N_product_re(t, p, s, n):
    if s == p:
        return 1
    elif s > p:
        return 0

    if n == len(t)-1:
        return 0

    sum = 0
    for i in range(n, len(t)):
        sum += found_N_product_re(t, p, s*t[i], i+1)

    return sum


t = [9, 2, 4, 5, 6, 3, 5]
#print(found_N_product_it(t, 6))
print(found_N_product_re(t, 6, 1, -1))

