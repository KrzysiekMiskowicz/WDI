#Krzysztof Miśkowicz

def distance(T):
    n = len(T)
    i_max = 0
    i_min = 0
    d = 0
    for i in range(1, n):
        if cmp(T, i, i_max):
            i_max = i
        if cmp(T, i_min, i):
            i_min = i
    return abs(i_max - i_min)

def cmp(T, a, b):
    n = len(T)
    c = 0
    while T[a][c] == T[b][c]:
        c += 1

    return T[a][c] > T[b][c]

T = [ [1, 1, 1, 1],
      [1, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0] ]

print(distance(T))