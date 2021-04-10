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


def last_element_before_cycle(p):
    if p is None or p.val is None:
        return 0

    addresses = []
    while p is not None:
        if p in addresses:
            i = addresses.index(p)
            if i == 0:
                return None
            else:
                return addresses[i-1]
        addresses.append(p)
        p = p.next

    return 0

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


head = a
for _ in range(5):
    a = a.next

addr = a

while a.next is not None:
    a = a.next

a.next = addr

a = head
l = (last_element_before_cycle(a))
print(l.val)