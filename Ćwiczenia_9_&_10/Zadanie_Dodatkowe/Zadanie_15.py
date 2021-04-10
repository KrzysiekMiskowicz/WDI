#odpowiednia imprementacja remove(p, v)
class node:
    def __init__(self, x = None):
        self.val = x
        self.next = None

def contain(p, v):
    if p is None or p.val is None:
        return False

    while p is not None:
        if p.val == v:
            return True
        p = p.next

    return False

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

def remove(p, v):
    if p is None:
        return

    prev = None
    while p is not None and p.val != v:
        prev = p
        p = p.next

    if p is None:
        return
    else:
        if prev is None:
            if p.next is None:
                p.val = None
            else:
                p.val = p.next.val
                p.next = p.next.next
        else:
            prev.next = p.next


def remove_repeats(p):
    if p is None or p.val is None:
        return

    while p.next is not None:
        while contain(p.next, p.val):
            remove(p.next, p.val)
        p = p.next


def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

a = node()
add(a, 1)
add(a, 1)
add(a, 5)
add(a, 5)
add(a, 8)
add(a, 45)
add(a, 45)
wypisz(a)
remove_repeats(a)
wypisz(a)
