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



def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

a = node()
add(a, 2)
add(a, 3)
add(a, 5)
wypisz(a)