LEN = 5
def slices(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    for L1 in range(1, LEN):
        for begin1 in range(n1-L1):
            sum1 = 0
            for i1 in range(begin1, begin1+L1):
                sum1 += t1[i1]

            L2 = LEN - L1
            for begin2 in range(n2-L2):
                sum2 = 0
                for i2 in range(begin2, begin2+L2):
                    sum2 += t2[i2]

                #print("L1 = {}, L2 = {}, b1 = {}, b2 = {}, s1 = {}, s2 = {}" .format(L1, L2, begin1, begin2, sum1, sum2))
                if is_multiple_of_power_of_natural_number(sum1+sum2):
                    return True

    return False


def is_multiple_of_power_of_natural_number(n):
    if n == 1:
        return True

    divider = 2
    while divider ** 2 <= n:
        power = 2
        while divider ** power <= n:
            if n == divider ** power:
                return True
            power += 1

        divider += 1

    return False


t1 = [1, 1, 1, 1, 1, 1]
t2 = [1, 1, 1, 1, 1, 1]

print(slices(t1, t2))