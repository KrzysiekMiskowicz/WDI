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

    while p.next is not None and p.next.val is not None:
        p = p.next

    p.next = node(v)
    p.next.prev = p

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

def remove_longest_substring(p):
    if p is None or p.val is None:
        return

    head = p
    ctr = 1
    max_ctr = 1
    index = 0
    max_index = None
    while p.next is not None:
        if p.next.val > p.val:
            ctr += 1
        else:
            if ctr > max_ctr:
                max_ctr = ctr
                max_index = index
            elif ctr == max_ctr:
                max_index = None
            ctr = 1
        index += 1
        p = p.next

    if max_index is not None:
        p = head
        if max_index+1 == max_ctr:
            for i in range(max_ctr):
                p = p.next

            head.val =p.val
            head.next = p.next
        else:
            for i in range(max_index-max_ctr):
                p = p.next

            head = p
            for i in range(max_ctr):
                p = p.next

            head.next = p.next

def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

a = node()
add(a, 1)
add(a, 0)
add(a, 5)
add(a, 8)
add(a, 9)
add(a, 5)
add(a, 8)
add(a, 45)
add(a, 4)
wypisz(a)
remove_longest_substring(a)
wypisz(a)
