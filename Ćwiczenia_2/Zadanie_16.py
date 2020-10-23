def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n < 2:
        return False
    divider = 5
    while n >= divider*divider:
        if n % divider == 0 or n % (divider + 2) == 0:
            return False
        divider += 6

    return True

# zakładam że liczby są wzajemnie różnocyforwe
def search_combination(n1, n2, search_n):

    while search_n > 0:
        search_digit = int(search_n % 10)
        find = False

        tmp_n1 = n1
        while tmp_n1 > 0:
            if search_digit == int(tmp_n1 % 10):
                tmp_n1 //= 10
                n1 = tmp_n1
                find = True
                break
            tmp_n1 //= 10

        tmp_n2 = n2
        if not find:
            tmp_n1 = n1
            while tmp_n2 > 0:
                if search_digit == int(tmp_n2 % 10):
                    tmp_n2 //= 10
                    n2 = tmp_n2
                    find = True
                    break
                tmp_n2 //= 10

        if not find:
            return False
        search_n //= 10

    return True

n1 = int(input("Podaj pierwsza liczbę -> "))
n2 = int(input("Podaj druga liczbę -> "))
for i in range(1, 10000):
    if is_prime(i):
        if search_combination(n1, n2, i):
            print(i)


