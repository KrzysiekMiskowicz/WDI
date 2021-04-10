def sfera(T, r):
    n = len(T)
    if n < 3:
        return False

    if length(T) < r:
        return True

    result = False
    for i in range(n):
        result |= sfera(T[:i]+T[i+1:], r)
    return result


def length(P):
    x, y, z = 0, 0, 0
    for i in P:
        x += i[0]
        y += i[1]
        z += i[2]
    x /= len(P)
    y /= len(P)
    z /= len(P)

    return (x**2 + y**2 + z**2)**0.5


T = [(1, 2, 1), (2, 2, 4), (1, 1, 2), (2, 4, 4)]
print(sfera(T, 10))
