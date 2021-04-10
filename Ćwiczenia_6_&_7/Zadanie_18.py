# do modyfikacji print
import random
t = [[random.randrange(1, 100) for _ in range(8)] for _ in range(8)]
last_digit = [[t[i][j] % 10 for j in range(8)] for i in range(8)]

def calculate_first_digit():
    global t
    first_digit = [[None for _ in range(8)] for _ in range(8)]
    n = len(t)
    for i in range(n):
        for j in range(n):
            l = 1
            while t[i][j] >= 10 ** l:
                l += 1

            first_digit[i][j] = (t[i][j] // (10 ** (l - 1)))

    return first_digit

first_digit = calculate_first_digit()

def board(r, c, destination):
    global t
    global first_digit
    global last_digit
    n = len(t)
    result = False

    if destination == 3:
        if c == r == n-1:
            print(r, c)
            return True

        if r != n-1 and first_digit[r+1][c] > last_digit[r][c]:
            result |= board(r+1, c, 3)

        if c != n-1 and first_digit[r][c+1] > last_digit[r][c] and not result:
            result |= board(r, c+1, 3)

        if r != n-1 and c != n-1 and first_digit[r+1][c+1] > last_digit[r][c] and not result:
            result |= board(r+1, c+1, 3)

        if result:
            print(r, c, destination)

    elif destination == 2:
        if c == 0 and r == n - 1:
            print(r, c)
            return True

        if r != n - 1 and first_digit[r + 1][c] > last_digit[r][c]:
            result |= board(r + 1, c, 2)

        if c != 0 and first_digit[r][c - 1] > last_digit[r][c] and not result:
            result |= board(r, c - 1, 2)

        if r != n - 1 and c != 0 and first_digit[r + 1][c - 1] > last_digit[r][c] and not result:
            result |= board(r + 1, c - 1, 2)

        if result:
            print(r, c, destination)

    elif destination == 1:
        if c == n - 1 and r == 0:
            print(r, c)
            return True

        if r != 0 and first_digit[r - 1][c] > last_digit[r][c]:
            result |= board(r - 1, c, 1)

        if c != n - 1 and first_digit[r][c + 1] > last_digit[r][c] and not result:
            result |= board(r, c + 1, 1)

        if r != 0 and c != n-1 and first_digit[r - 1][c + 1] > last_digit[r][c] and not result:
            result |= board(r - 1, c + 1, 1)

        if result:
            print(r, c, destination)

    elif destination == 0:
        if c == r == 0:
            print(r, c)
            return True

        if r != 0 and first_digit[r - 1][c] > last_digit[r][c]:
            result |= board(r - 1, c, 0)

        if c != 0 and first_digit[r][c - 1] > last_digit[r][c] and not result:
            result |= board(r, c - 1, 0)

        if r != 0 and c != 0 and first_digit[r - 1][c - 1] > last_digit[r][c] and not result:
            result |= board(r - 1, c - 1, 0)

        if result:
            print(r, c, destination)

    return result


n = len(t)
for i in range(n):
    for j in range(n):
        print(t[i][j], end=" ")

    print()
print()

result = False
for i in range(4):
    result |= board(3, 3, i)

print(result)