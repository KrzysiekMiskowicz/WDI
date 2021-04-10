'''
def substring(t, s):
    if s == 0:
        return True

    n = len(t)
    if n == 1:
        return t[0][0] == s

    result = False
    for x in range(n):
        p = [[None for _ in range(n - 1)] for _ in range(n - 1)]
        r = 0
        for i in range(n):
            if i != x:
                for j in range(1, n):
                    p[r][j-1] = t[i][j]
                r += 1

        result |= substring(p, s-t[0][x]) or substring(p, s)

    return result
'''

'''
n = len(t)
pom = [[None for _ in range(n-1)] for _ in range(n-1)]
c = 0
r = 0
for i in range(3):
    if i != 1:
        r = 0
        for j in range(3):
            if j != 1:
                pom[r][c] = t[i][j]
                r += 1
        c += 1

print(pom)
'''

def substring(t, s, crossed = [], row = 0):
    if s == 0:
        if len(crossed) == 0:
            return False
        else:
            return True

    if s < 0:
        return False

    n = len(t)
    if row == n:
        return False

    result = substring(t, s, crossed, row+1)
    for col in range(n):
        if col not in crossed:
            result = result or substring(t, s-t[row][col], crossed+[col], row+1)

    return result



t = [[1, 2, 3, 4],
     [4, 1, 2, 3],
     [3, 4, 1, 2],
     [2, 3, 4, 1]]
print(substring(t, 0, []))

