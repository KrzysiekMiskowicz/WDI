# zmienic obliczanie pierwszej i ostatniej cyfry
import random
t = [[random.randrange(1, 100) for _ in range(8)] for _ in range(8)]
last_digit = [[t[i][j] % 10 for j in range(8)] for i in range(8)]

def calculate_first_digit():
    global t
    first_digit = [[None for j in range(8)] for i in range(8)]
    n = len(t)
    for i in range(n):
        for j in range(n):
            l = 1
            while t[i][j] >= 10 ** l:
                l += 1

            first_digit[i][j] = (t[i][j] // (10 ** (l - 1)))

    return first_digit

first_digit = calculate_first_digit()

def board(r, c):
    global t
    global first_digit
    global last_digit
    n = len(t)
    if c == r == n-1:
        return True

    result = False
    if r != n-1 and first_digit[r+1][c] > last_digit[r][c]:
        result |= board(r+1, c)

    if c != n-1 and first_digit[r][c+1] > last_digit[r][c]:
        result |= board(r, c+1)

    if c != n-1 and r != n-1 and first_digit[r+1][c+1] > last_digit[r][c]:
        result |= board(r+1, c+1)

    return result


n = len(t)
for i in range(n):
    for j in range(n):
        print(t[i][j], end=" ")

    print()
print()

print(board(6, 7))