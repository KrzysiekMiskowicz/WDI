iterations = 0
last_operation = -1

def zad2(X, Y, n):
    global iterations
    global last_operation

    if X == Y:
        return 1

    if iterations >= n:
        return 0

    sum = 0

    A_move = last_operation != 0
    B_move = last_operation != 1
    C_move = last_operation != 2

    if A_move:
        last_operation = 0
        iterations += 1
        sum += zad2(X+3, Y, n)
        iterations -= 1

    if B_move:
        last_operation = 1
        iterations += 1
        sum += zad2(2*X, Y, n)
        iterations -= 1

    if C_move:
        last_operation = 2
        iterations += 1
        sum += zad2(increment_even_digits(X), Y, n)
        iterations -= 1

    return sum

def increment_even_digits(n):
    i = 0
    result = 0
    while n != 0:
        if (n % 10) % 2 == 0:
            result += (n % 10 + 1) * 10 ** i
        else:
            result += (n % 10) * 10 ** i
        i += 1
        n //= 10

    return result

print(zad2(11, 31, 4))