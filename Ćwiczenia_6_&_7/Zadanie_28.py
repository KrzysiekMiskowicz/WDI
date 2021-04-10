#'''
def divide_set(t, f = [[]]):
    n = len(t)
    if n == 0:
        if len(f) == 1:
            return False
        s = ones_in_binary(f[0])
        for i in f:
            if ones_in_binary(i) != s:
                return False
        print(f)
        return True

    result = False
    for i in f:
        i.append(t[0])
        result |= divide_set(t[1:], f)
        i.remove(i[-1])

    result |= divide_set(t[1:], f+[[t[0]]])
    return result
#'''

def ones_in_binary(t):
    ones = 0
    for b in t:
        if b < 1:
            continue
        while b != 0:
            if b % 2 == 1:
                ones += 1
            b //= 2

    return ones


#print(ones_in_binary([15]))
t = [2, 3, 5, 7, 15]
print(divide_set(t))