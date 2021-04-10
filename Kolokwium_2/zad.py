#Krzysztof Miśkowicz

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

n_numbers = 1

def divide(N):
    global n_numbers
    if is_primary(N) and is_primary(n_numbers):
            return True

    digits = 1
    while N >= 10 ** digits:
        digits += 1

    if digits == 1:
        return False

    result = False
    for i in range(1, digits):
        if is_primary(N % (10 ** i)):
            n_numbers += 1
            result = result or divide(N // (10 ** i))
            n_numbers -= 1

    return result

print(divide(273)) # True, podział 2|7|3
print(divide(22222)) # True, podział 2|2|2|2|2
print(divide(23672)) # True, podział 23|67|2
print(divide(2222)) # False
print(divide(21722)) # False
