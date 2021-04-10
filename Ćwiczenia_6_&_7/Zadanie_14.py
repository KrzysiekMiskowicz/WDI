def hetman(t, r):
    n = len(t)

    if r == n:
        for i in range(n):
            for j in range(n):
                if t[i][j]:
                    print("+", end=" ")
                else:
                    print("0", end=" ")
            print()
        print()
        return

    for i in range(n):
        if is_move_possible(t, r, i):
            t[r][i] = True
            hetman(t, r+1)
            t[r][i] = False
    return

#można zamiast tego policzyć
#desmos.com
def is_move_possible(t, r, c):
    n = len(t)
    for i in range(r):
        if t[i][c]:
            return False

    i = 1
    j = 1
    while r + i < n and c + j < n:
        if t[r+i][c+j]:
            return False
        i += 1
        j += 1

    i = 1
    j = 1
    while r - i >= 0 and c - j >= 0:
        if t[r-i][c-j]:
            return False
        i += 1
        j += 1

    i = 1
    j = 1
    while r - i >= 0 and c + j < n:
        if t[r-i][c+j]:
            return False
        i += 1
        c += 1

    i = 1
    j = 1
    while r + i < n and c - j >= 0:
        if t[r+i][c-j]:
            return False
        i += 1
        j += 1

    return True

t = [[False for _ in range(8)] for _ in range(8)]


hetman(t, 0)
