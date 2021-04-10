def best_rooks(t):
    n = len(t)
    fields = [count_line(t, i//n) + count_column(t, i%n) for i in range(n*n)]
    #for i in fields:
        #print(i)
    l1, l2, c1, c2 = None, None, None, None
    max_sum = 1
    for i in range(n*n-1):
        for j in range(i+1, n*n):
            current_sum = fields[i] + fields[j]

            if i//n == j//n:
                current_sum -= count_line(t, i//n)
            elif i%n == j%n:
                current_sum -= count_column(t, i%n)
            else:
                current_sum -= t[i//n][i%n] + t[j//n][j%n] + t[i//n][j%n] + t[i//n][j%n]

            current_sum -= t[i//n][i%n] + t[j//n][j%n]
            if current_sum > max_sum:
                max_sum = current_sum
                l1, l2, c1, c2 = i//n, j//n, i%n, j%n

    print('({}, {}) ({}, {})'.format(c1, l1, c2, l2))
    return max_sum


def count_line(t, l):
    sum = 0
    for i in range(len(t)):
        sum += t[l][i]

    return sum


def count_column(t, c):
    sum = 0
    for i in range(len(t)):
        sum += t[i][c]

    return sum


t =[[0, 0, 0, 4, 0],
    [8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4],
    [0, 0, 0, 4, 0]]

print(best_rooks(t))
