'''
def min_sum(t, l_min, sum, n, c):
    if n == len(t):
        l = 0
        s = 0
        index = 0
        for i in range(len(t)):
            if c[i] == '1':
                s += t[i]
                l += 1
                index += i

        if index == s and (l_min is None or l < l_min) and l != 0:
            l_min = l
            sum = s
            print(sum, l_min)

    else:
        min_sum(t, l_min, sum, n+1, c+"0")
        min_sum(t, l_min, sum, n+1, c+"1")

t = [ 1, 7, 3, 5, 11, 2 ]
min_sum(t, None, None, 0, "")

# można tablice ustawić nie jako arguent funkcji, a funkcje wykonuje się na dwóch argumentach
# żeby wypisywać można użyć 3 argumentu - tablicy wybranych tab + t[]
'''

def min_sum(t, p, min_i, i):
    if len(p) > 0 and is_equal(t, p):
        min_i = min(min_i, len(p))
        print(p)
        return min_i

    if len(p) >= min_i-1:
        return min_i

    n = len(t)
    result = 10
    for j in range(i, n):
        result = min(result, min_sum(t, p+[j], min_i, j+1))

    return result

def is_equal(t, i):
    sum_t = 0
    sum_i = 0
    for a in i:
        sum_t += t[a]
        sum_i += a

    return sum_t == sum_i

t = [ 1, 7, 3, 5, 11, 2 ]
print(min_sum(t, [], 10, 0))