class node:
    def __init__(self, x = None):
        self.val = x
        self.next = None

def add(p, v):
    if p.val is None:
        p.val = v
        return

    prev = None
    while p is not None and p.val is not None:
        prev = p
        p = p.next

    if prev is None:
        p.next = node(v)
    else:
        prev.next = node(v)


def addition(p1, p2):
    n1 = list_to_array(p1)
    n2 = list_to_array(p2)
    L1 = len(n1)
    L2 = len(n2)
    overflow = 0
    s = [0 for _ in range(max(L1, L2))]
    for i in range(max(L1, L2)):
        s[i] = overflow
        if L1 > i:
            s[i] += n1[i]
        if L2 > i:
            s[i] += n2[i]

        overflow = s[i] // 10
        s[i] %= 10

    if overflow > 0:
        s.append(overflow)

    s.reverse()
    return array_to_list(s)

def list_to_array(p):
    t = []
    while p is not None:
        t.append(p.val)
        p = p.next

    t.reverse()
    return t

def array_to_list(t):
    n = len(t)
    if n == 0:
        return
    p = node(t[0])
    head = p
    for i in range(1, n):
        p.next = node(t[i])
        p = p.next

    return head

def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


a = node()
add(a, 1)
add(a, 9)
add(a, 9)
wypisz(a)
b = node()
add(b, 1)
add(b, 2)
wypisz(b)
wypisz(addition(a, b))