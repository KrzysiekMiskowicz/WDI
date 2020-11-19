ZERO = 48
a = 97
"""
n = int(input("Podaj liczbe -> "))
for i in range(2, 16+1):
    print(i, end=" -> ")
    digit_value = 0
    while i**digit_value <= n:
        digit_value += 1

    n_str = ""
    digit_value -= 1
    while digit_value >= 0:
        if (n // i**digit_value) % i >= 10:
            n_str += chr(a + ((n // i**digit_value) % i) % 10)
        else:
            n_str += chr(ZERO + (n // i**digit_value) % i)
        digit_value -= 1

    print(n_str)
"""

n = int(input("Podaj liczbe -> "))
for i in range(2, 16+1):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 'a', 'b', 'c', 'd', 'e', 'f']
    n_str = ""
    n_temp = n
    while n_temp > 0:
        n_str += digits[n_temp % i]
        n_temp //= i

    reversed(n_str)
