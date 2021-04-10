#[x1, x2, y1, y2]
#wycinek zbioru (t[:i] + t[i + 1:])
def find_squares(t):
    n = len(t)
    if n == 2:
        if are_squares_seperate(t) and sum_fields(t) == 5:
            return True
        else:
            return False

    result = False
    for i in range(n):
        #mem = t[i]
        #t.remove(t[i])
        #result |= find_squares(t)
        #t.insert(i, mem)
        result |= find_squares(t[:i] + t[i + 1:])

    return result


def are_squares_seperate(t):
    n = len(t)
    for i in range(n-1):
        for j in range(i+1, n):
            if t[j][0] < t[i][0] < t[j][1] or t[j][0] < t[i][1] < t[j][1]:
                if t[j][2] < t[i][2] < t[j][3] or t[j][2] < t[i][3] < t[j][3]:
                    return False

    return True

def sum_fields(t):
    s = 0
    for i in t:
        s += (i[1]-i[0]) * (i[3]-i[2])

    return s


t = [(1, 3, 1, 3), (4, 5, 6, 7), (2, 4, 2, 4)]
print(find_squares(t))