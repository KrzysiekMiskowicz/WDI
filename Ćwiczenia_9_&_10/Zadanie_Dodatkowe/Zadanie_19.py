class node:
    def __init__(self, x = None):
        self.val = x
        self.next = None


def contain(p, v):
    if p is None or p.val is None:
        return False

    while p is not None and p.val is not None:
        if p.val == v:
            return True
        p = p.next

    return False


def add(p, v):
    if p.val is None:
        p.val = v
        return

    prev = None
    while p is not None and p.val is not None:
        prev = p
        p = p.next

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

def list(p):
    while p is not None and p.val is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def is_cyclic(p):
    if p is None or p.val is None:
        return False

    addresses = []
    while p is not None:
        if p in addresses:
            return True
        addresses.append(p)
        p = p.next

    return False

a = node(1)
add(a, 3)
add(a, 3)
add(a, 3)
add(a, 5)
add(a, 7)
add(a, 11)
add(a, 13)
add(a, 13)
add(a, 1)
add(a, 2)
add(a, 2)
add(a, 2)
add(a, 2)
add(a, 3)
list(a)
print(is_cyclic(a))


head = a
for _ in range(5):
    a = a.next

addr = a

while a.next is not None:
    a = a.next

a.next = addr

a = head
print(is_cyclic(a))
