class node:
    def __init__(self, x = None):
        self.val = x
        self.next = None

def add(p, v):
    prev = None
    while p is not None and cmp(p.val, v) < 1:
        if cmp(p.val, v) == 0:
            return
        prev = p
        p = p.next

    if p is None:
        if prev is None:
            p.val = v
        else:
            prev.next = node(v)
    else:
        if prev is None:
            prev = node(p.val)
            p.val = v
            p.next = prev
        else:
            prev.next = node(v)
            prev.next.next = p


def cmp(s1, s2):
    L1 = len(s1)
    L2 = len(s2)
    for i in range(min(L1, L2)):
        if ord(s1[i]) > ord(s2[i]):
            return 1
        elif ord(s1[i]) < ord(s2[i]):
            return -1

    if L1 == L2:
        return 0
    elif L1 > L2:
        return 1
    else:
        return -1

def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


a = node("2")
add(a, "da")
add(a, "da")
add(a, "c")
wypisz(a)
