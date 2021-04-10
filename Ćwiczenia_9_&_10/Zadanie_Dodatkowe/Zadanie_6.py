#odpowiednia implementacja funkcji add_or_remove -> poprawne usuwanie, moze poza head
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

def remove(p):
    if p.val is None:
        return

    prev = None
    while p.next is not None:
        prev = p
        p = p.next

    if prev is None:
        p.val = None
    else:
        prev.next = None


def remove_or_add(p, v):
    prev = None
    head = p
    while p is not None and p.val != v:
        prev = p
        p = p.next

    if p is None:
        prev.next = node(v)
    else:
        if prev is None:
            if head.next is None:
                head.val = None
            else:
                head.val = head.next.val
                head.next = head.next.next
        else:
            prev.next = p.next

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
remove_or_add(a, 6)
wypisz(a)
remove_or_add(a, 3)
wypisz(a)
remove_or_add(a, 2)
wypisz(a)
remove_or_add(a, 6)
wypisz(a)
remove_or_add(a, 5)
print(a.val)