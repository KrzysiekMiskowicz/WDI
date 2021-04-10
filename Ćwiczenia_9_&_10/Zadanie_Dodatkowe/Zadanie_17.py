#odpowiednia imprementacja remove(p, v)
class node:
    def __init__(self, begin = None, end = None):
        self.begin = begin
        self.end = end
        self.next = None

def contain(p, v):
    if p is None or p.begin is None:
        return None

    while p is not None:
        if p.begin <= v <= p.end:
            return [p.begin, p.end]
        p = p.next

    return None

def add(p, begin, end):
    if p is None or p.begin is None:
        p.begin = begin
        p.end = end
        return

    prev = None
    while p is not None:
        prev = p
        p = p.next

    prev.next = node(begin, end)

def remove(p, v):
    if p is None:
        return

    prev = None
    while p is not None and not (p.begin <= v <= p.end):
        prev = p
        p = p.next

    if p is None:
        return
    else:
        if prev is None:
            if p.next is None:
                p.begin = None
            else:
                p.begin = p.next.begin
                p.end = p.next.end
                p.next = p.next.next
        else:
            prev.next = p.next

def merge(p):
    if p is None or p.begin is None:
        return

    while p is not None:
        if contain(p.next, p.begin) is not None:
            p.begin = min(p.begin, contain(p.next, p.begin)[0])
            p.end = max(p.end, contain(p.next, p.begin)[1])
            remove(p.next, p.begin)
            continue
        if contain(p.next, p.end) is not None:
            p.begin = min(p.begin, contain(p.next, p.end)[0])
            p.end = max(p.end, contain(p.next, p.end)[1])
            remove(p.next, p.end)
            continue
        p = p.next


def wypisz(p):
    while p is not None and p.begin is not None:
        print("[", p.begin, ",", p.end, "]", end=" ")
        p = p.next
    print()

a = node()
add(a, 6, 12)
add(a, 1, 5)
add(a, 4, 5)
add(a, 5, 6)
add(a, 1, 3)
wypisz(a)
merge(a)
wypisz(a)

