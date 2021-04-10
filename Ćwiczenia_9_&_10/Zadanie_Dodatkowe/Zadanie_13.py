class node:
    def __init__(self, x = None):
        self.val = x
        self.prev = None
        self.next = None


def add(p, v):
    if p.val is None:
        p.val = v
        return

    while p.next is not None and p.next.val is not None:
        p = p.next

    p.next = node(v)
    p.next.prev = p

def remove(p, v):
    if p is None or p.val is None:
        return

    while p.next is not None and p.val != v:
        p = p.next

    if p.val == v:
        if p.prev is not None:
            p.prev.next = p.next
        else:
            if p.next is None:
                p.val = None
                return
            else:
                p.val = p.next.val
                p.next = p.next.next
                p.next.prev = p
                return
        if p.next is not None:
            p.next.prev = p.prev

'''
def remove_zad_13(p): # nie dziala usuwanie po przesuwania (chyba dwoch pod rzad), powstaje dziwny cykl dla p i p.next
    head = p
    while p is not None and p.val is not None:
        if count_ones(binary_system(p.val)) % 2 == 1:
            print("Przed usunieciem:", p.val)
            wypisz(head)
            wypisz(p)
            remove(head, p.val)
            print("Po usunieciu:", p.val)
            wypisz(head)
            wypisz(p)
            if p.prev is not None:
                print(p.prev.val, p.prev.next.val)
        else:
            print("Przed przejsciem:", p.val)
            wypisz(head)
            wypisz(p)
            p = p.next
            print("Po przejsciu:", p.val)
            wypisz(head)
            wypisz(p)
            if p.prev is not None:
                print(p.prev.val, p.prev.next.val)
'''

def remove_zad_13(p):
    head = p
    while p is not None and p.val is not None:
        if count_ones(binary_system(p.val)) % 2 == 1:
            remove(head, p.val)
            if p.prev is not None:
                p = p.prev
        else:
            p = p.next

def binary_system(n):
    result = 0
    waga = 0
    while n != 0:
        result += (n % 2) * 10 ** waga
        waga += 1
        n //= 2

    return result


def count_ones(n):
    ones = 0
    while n != 0:
        if n % 10 == 1:
            ones += 1
        n //= 10

    return ones


def wypisz(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

def wypisz_odwr(p):
    while p.next is not None:
        p = p.next
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.prev
    print()


a = node()
add(a, 1)
add(a, 2)
add(a, 5)
add(a, 6)
add(a, 10)
add(a, 11)
add(a, 14)
wypisz(a)
'''
wypisz_odwr(a)
remove(a, 1)
wypisz(a)
wypisz_odwr(a)
remove(a, 14)
wypisz(a)
wypisz_odwr(a)
'''
#remove_zad_13(a)
remove_zad_13(a)
#remove(a, 1)
wypisz(a)
