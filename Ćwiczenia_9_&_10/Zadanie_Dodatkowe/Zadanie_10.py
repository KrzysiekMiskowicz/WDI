#odpowiednia imprementacja remove(p, v)
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


def remove_dividers(p):
    if p is None:
        return

    while p.next is not None:
        if p.next.val % p.val == 0:
            prev = p
            p = p.next
            remove(prev, prev.val)
        else:
            p = p.next



def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


a = node()
add(a, 2)
add(a, 4)
add(a, 5)
add(a, 10)
wypisz(a)
remove_dividers(a)
wypisz(a)

