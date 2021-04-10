def multi(t):
    n = len(t)
    l_max = 0
    for i in range(n//2 + 1):
        l_max = max(l_max, repeats(t, i+1))

    return l_max

def repeats(t, p):
    n = len(t)
    if n % p != 0:
        return 0
    for i in range(n):
        if t[i] != t[i % p]:
            return 0

    return p

t = [1, 2, 3, 1, 2, 3]
print(multi(t))