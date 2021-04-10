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


def remove_in_triple_system(p):
    if p is None:
        return

    while p is not None:
        n = triple_system(p.val)
        if cmp_ones_and_twos(n):
            rem = p
            p = p.next
            remove(rem, rem.val)
        else:
            p = p.next

def triple_system(n):
    result = 0
    waga = 0
    while n != 0:
        result += (n % 3) * 10**waga
        waga += 1
        n //= 3

    return result

def cmp_ones_and_twos(n):
    ones = 0
    twos = 0
    while n != 0:
        if n % 10 == 1:
            ones += 1
        elif n % 10 == 2:
            twos += 1
        n //= 10

    return ones > twos


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
remove_in_triple_system(a)
wypisz(a)
