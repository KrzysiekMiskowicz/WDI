class node:
    def __init__(self, x = None):
        self.val = x
        self.next = None

#tworzy ciąg niemalejący
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

def remove(p):
    if p is None or p.val is None:
        return

    prev = None
    while p is not None:
        if prev is None:
            prev = p
        else:
            if prev.val > p.val:
                prev.next = p.next
            else:
                prev = p
        p = p.next

    if prev is None:
        p.val = None
    else:
        prev.next = None


def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


a = node()
add(a, 2)
add(a, 1)
add(a, 5)
add(a, 1)
add(a, 4)
wypisz(a)
remove(a)
wypisz(a)

