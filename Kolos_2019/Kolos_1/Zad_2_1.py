def slices(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    LEN = min(n1, n2)
    for LEN in range(1, LEN+1):
        for begin1 in range(n1-LEN):
            sum1 = 0
            for i1 in range(begin1, begin1+LEN):
                sum1 += t1[i1]

            for begin2 in range(n2-LEN):
                sum2 = 0
                for i2 in range(begin2, begin2+LEN):
                    sum2 += t2[i2]

                print("L = {}, b1 = {}, b2 = {}, s1 = {}, s2 = {}" .format(LEN, begin1, begin2, sum1, sum2))
                if is_product_of_two_primary_numbers(sum1+sum2):
                    return True

    return False


def is_primary_number(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    divider = 6
    while divider * divider <= n:
        if n % (divider - 1) == 0 or n % (divider + 1) == 0:
            return False
        divider += 6

    return True


def is_product_of_two_primary_numbers(n):
    divider = 2
    while divider * divider <= n:
        if n % divider == 0:
            if is_primary_number(divider) and is_primary_number(n // divider):
                return True
        divider += 1

    return False


t1 = [1, 1, 1, 1, 1, 1]
t2 = [1, 1, 1, 1, 1, 1]
print(slices(t1, t2))
