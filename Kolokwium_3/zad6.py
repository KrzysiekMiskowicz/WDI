#Krzysztof Miśkowicz

#sprawdzam czy kolejne elementy pierwszej listy należą do dwóch pozostałych, jeśli tak jest to zostawiam ten element,
#(przez to moja zwracana lista będzie zawierać te same miejsca w pamięci co lista z1, ale nie było napisane że tak nie można)
#jeśli nie to go usuwam. Na koniec zwracam listę która zawiera wspólne elementy

class Node:
    def __init__(self, val):
        self.val = val
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

    p.next = Node(v)
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


def iloczyn(z1, z2, z3):

    if z1 is None or z1.val is None:
        return None

    head = z1
    while z1 is not None and z1.val is not None:
        if contain(z2, z1.val) and contain(z3, z1.val):
            z1 = z1.next
        else:
            remove(z1, z1.val)

    return head


def list(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()

'''
Przykładowy test
z1 = Node(1)
add(z1, 3)
add(z1, 4)
add(z1, 5)
add(z1, 6)

z2 = Node(1)
add(z2, 3)
add(z2, 4)

z3 = Node(7)
add(z3, 4)
add(z3, 5)

list(z1)
list(z2)
list(z3)

z4 = iloczyn(z1, z2, z3)
list(z4)
'''