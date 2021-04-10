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


def increment(p):
    if p.val is None:
        p.val = 1
        return

    head = p
    digits = 0
    while p is not None:
        digits += 1
        p = p.next

    while digits > 0 and increment_digit(head, digits-1):
        digits -= 1
        if digits == 0:
            add(head, 0)
            head.val = 1
            p = head.next
            while p is not None:
                p.val = 0
                p = p.next
            return


def increment_digit(p, n):
    for i in range(n):
        p = p.next

    p.val += 1
    if p.val >= 10:
        p.val %= 10
        return True
    else:
        return False


def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


a = node()
add(a, 8)
add(a, 9)
wypisz(a)
increment(a)
wypisz(a)
