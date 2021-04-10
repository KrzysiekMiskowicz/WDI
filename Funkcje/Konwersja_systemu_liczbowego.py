def five_system(n):
    result = 0
    while n != 0:
        result *= 5
        result += n % 5
        n //= 5