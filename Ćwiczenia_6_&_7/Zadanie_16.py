def merge_numbers(n1, n2, number):
    if n1 == n2 == 0:
        if is_primary(number):
            print(number, "+")
            return 1
        else:
            print(number)
            return 0
    l1 = 1
    while n1 >= 10 ** l1:
        l1 += 1

    l2 = 1
    while n2 >= 10 ** l2:
        l2 += 1

    primary_numbers = 0
    if n1 != 0:
        # 27 -> 2, 7
        primary_numbers += merge_numbers(n1 % 10 ** (l1 - 1), n2, 10*number + (n1 // (10 ** (l1 - 1))))
    if n2 != 0:
        primary_numbers += merge_numbers(n1, n2 % 10 ** (l2 - 1), 10*number + (n2 // (10 ** (l2 - 1))))

    return primary_numbers

def is_primary(n):
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


print(merge_numbers(123, 75, 0))
