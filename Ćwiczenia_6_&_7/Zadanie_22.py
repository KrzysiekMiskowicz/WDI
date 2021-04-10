#jeśli budujemy tablicę w której elementy się nie mg powtarząć, to występuje kłopot zerowego elementu (0, n) zamiast (1, n)
'''
#budowanie
def find_resistance(t, x, r = []):
    n = len(r)
    if n == 3:
        if resistance(r, x):
            print(r)
        return resistance(r, x)
    result = False
    k = len(t)
    if n == 0:
        s = 0
    else:
        s = 1
    for i in range(s, k+n-2):
        result |= find_resistance(t[i:], x, r+[t[i]])

    return result
'''
#usuwanie
'''
def find_resistance(t, x):
    n = len(t)
    if n < 3:
        return False
    elif n == 3:
        return resistance(t, x)
    result = False
    for i in range(n):
        mem = t[i]
        t.remove(t[i])
        result |= find_resistance(t, x)
        t.insert(i, mem)

    return result
'''

def find_resistance(t, val, r=[]):
    if len(r) == 3:
        return resistance(r, val)

    n = len(t)
    result = False
    for i in range(n-3+len(r)):
        result = result or find_resistance(t[i:], val, r+[t[i]])

    return result


def resistance(r, x):
    r1, r2, r3 = r[0], r[1], r[2]
    if r1+r2+r3 == x:
        return True
    elif r1+r2+r3 < x:
        return False
    if ((r1*r2)*r3/(r1+r2))/(((r1*r2)/(r1+r2))+r3) == x:
        return True
    elif ((r1*r2)*r3/(r1+r2))/(((r1*r2)/(r1+r2))+r3) > x:
        return False
    if r1+(r2*r3)/(r2+r3) == x or r2+(r1*r3)/(r1+r3) == x or r3+(r2*r1)/(r2+r1) == x:
        return True
    if (r1*(r2*r3)/(r2+r3))/(((r2*r3)/(r2+r3))+r1) == x or (r2*(r1*r3)/(r1+r3))/(((r1*r3)/(r1+r3))+r2) == x or (r3*(r2*r1)/(r2+r1))/(((r2*r1)/(r2+r1))+r3) == x:
        return True
    return False


t = [3, 3, 2, 4, 2, 5, 10]
print(find_resistance(t, 5))