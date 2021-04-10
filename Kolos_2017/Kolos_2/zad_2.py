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

def rek(sub, left):
    n = len(left)
    if n == 0:
        print(sub)

    m = len(sub)
    last = sub[m-1]
    last_prime = is_prime(last)

    for i in range(n):
        if not (is_prime(left[i]) and last_prime) and abs(last - left[i]) >= 2:
            rek(sub+[left[i]], left[0:i] + left[i+1:n])

rek([1], [2, 3, 4, 5, 6, 7, 8, 9])

