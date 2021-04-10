#to samo co zad 3_1
def find_kings(t, kings=[]):
    n = len(t)
    k = len(kings)
    if n == k:
        return count_fields(t, kings)

    result = False
    if k == 0:
        for i in range(n):
            result = result or find_kings(t, [i])
    else:
        for i in range(n):
            if abs(kings[-1] - i) > 1:
                result = result or find_kings(t, kings+[i])

    return result

def count_fields(t, k):
    n = len(t)
    s = 0
    for i in range(n):
        s += t[i][k[i]]

    return s == 0



t =[[1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, -8, 5] ]

print(find_kings(t))