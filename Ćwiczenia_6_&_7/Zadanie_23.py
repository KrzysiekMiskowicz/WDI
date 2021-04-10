#permutowanie po dwóch zbiorach na raz -> wyszkorzystać dwa zbiory ;)
MAX = 10
def min_length(T, P1 = [], P2 = [], n = 0):
    l = len(T)
    if n == l:
        if len(P1) == 0 or len(P2) == 0 or P1 == P2:
            return MAX
        else:
            #print("P1 -> ", P1, "P2 -> ", P2)
            return length(P1, P2)

    l_min = MAX
    l_min = min(l_min, min_length(T, P1+[T[n]], P2+[T[n]], n+1))
    l_min = min(l_min, min_length(T, P1+[T[n]], P2, n+1))
    l_min = min(l_min, min_length(T, P1, P2+[T[n]], n+1))
    l_min = min(l_min, min_length(T, P1, P2, n+1))

    return l_min


def length(P1, P2):
    x_p1, y_p1, x_p2, y_p2 = 0, 0, 0, 0
    for i in P1:
        x_p1 += i[0]
        y_p1 += i[1]
    x_p1 /= len(P1)
    y_p1 /= len(P1)

    for i in P2:
        x_p2 += i[0]
        y_p2 += i[1]
    x_p2 /= len(P2)
    y_p2 /= len(P2)

    return ((x_p1-x_p2)**2 + (y_p1-y_p2)**2)**0.5


T = [(1, 2), (2, 2)]
print(min_length(T))
