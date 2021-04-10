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


def remove_every_second(p):
    if p.val is None:
        return

    while p is not None and p.next is not None:
        p.next = p.next.next
        p = p.next


def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


a = node()
add(a, 1)
add(a, 2)
add(a, 3)
add(a, 4)
add(a, 5)
add(a, 6)
add(a, 7)
add(a, 8)
add(a, 9)
wypisz(a)
remove_every_second(a)
wypisz(a)
