'''
def king_moves(t, k, s, n):
    if k < 0 or k >= len(t):
        return -1

    s += t[n][k]
    if n == len(t)-1:
        return s

    sum = [None for _ in range(3)]
    for i in range(3):
        sum[i] = king_moves(t, k+i-1, s, n+1)

    min = None
    for i in sum:
        if i != -1 and (min is None or i < min):
            min = i

    return min
'''

def king_moves(t, w = 0, k = 0, suma = 0):
    suma += t[w][k]
    if w == len(t)-1:
        return suma

    min_suma = king_moves(t, w+1, k, suma)
    if k != 0:
        min_suma = min(min_suma, king_moves(t, w+1, k-1, suma))
    if k != len(t)-1:
        min_suma = min(min_suma, king_moves(t, w+1, k+1, suma))

    return min_suma


t =[[1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8]]

print(king_moves(t, 2, 2, 0))

#skoczek varensdorfa