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
    while p is not None and p.val <= v:
        prev = p
        p = p.next

    if p is None:
        prev.next = node(v)
    else:
        if prev is None:
            prev = node(v)
            prev.next = prev
            prev.val, p.val = p.val, prev.val
            prev.next, p.next = p.next, prev.next
            #trzeba uzyc przypisania pol klasy, zamiat calych instancji (prev, p = p, prev) -> spowodowane mutowalnoscia
        else:
            adr = prev.next
            prev.next = node(v)
            prev.next.next = adr

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
        return 0
    counter = 0

    while p.next is not None:
        while contain(p.next, p.val):
            counter += 1
            remove(p.next, p.val)
        p = p.next

    return counter

def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

a = node()
add(a, 1)
add(a, 0)
add(a, 5)
add(a, 5)
add(a, 8)
add(a, 45)
add(a, 45)
add(a, 45)
wypisz(a)
print(remove_repeats(a))
wypisz(a)
