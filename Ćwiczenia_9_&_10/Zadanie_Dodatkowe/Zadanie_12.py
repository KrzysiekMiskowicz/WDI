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


def move_to_head(p): #sortuje liste w kolejnosci od liczb których postać ósemkowa zawiera parzystą liczbę piątek
    if p is None:
        return

    head = p
    new_head = None
    new_p = None
    while p is not None and p.val is not None:
        if count_fives(octal_system(p.val)) % 2 == 0:
            if new_head is None:
                new_head = node(p.val)
                new_p = new_head
            else:
                new_p.next = node(p.val)
                new_p = new_p.next
        p = p.next

    p = head
    while p is not None and p.val is not None:
        if count_fives(octal_system(p.val)) % 2 != 0:
            if new_head is None:
                new_head = node(p.val)
                new_p = new_head
            else:
                new_p.next = node(p.val)
                new_p = new_p.next
        p = p.next
    return new_head


def octal_system(n):
    result = 0
    waga = 0
    while n != 0:
        result += (n % 8) * 10**waga
        waga += 1
        n //= 8

    return result

def count_fives(n):
    fives = 0
    while n != 0:
        if n % 10 == 5:
            fives += 1
        n //= 10

    return fives


def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

a = node()
add(a, 1)
add(a, 5)
add(a, 6)
add(a, 8)
add(a, 45)
wypisz(a)
wypisz(move_to_head(a))
wypisz(a)
