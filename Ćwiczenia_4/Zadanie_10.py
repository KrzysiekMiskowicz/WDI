MAX = 4

def is_0_in_every_column_and_line(t):
    for i in range(MAX):
        in_line = False
        for j in range(MAX):
            if t[i][j] == 0:
                in_line = True
                break

        if not in_line:
            return False

    return True

t = [[1, 2, 3, 1],
    [1, 2, 3, 0],
    [1, 2, 3, 0],
    [1, 2, 3, 0]]

print(is_0_in_every_column_and_line(t))

