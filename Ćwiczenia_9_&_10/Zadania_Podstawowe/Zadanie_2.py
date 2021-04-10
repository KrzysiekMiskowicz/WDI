#posortować
# w obiektowym podejściu można w tablicy first przechowywać za pomocą przypisania self.first = p
class node:
    def __init__(self, index = 0, val = 0):
        self.val = val
        self.index = index
        self.next = None


#nie zmienia wartosci dla t = None (mutowalnosc  w pythonie)
def init(t):
    t.val = None
    str(t)


def value(t, n):
    while t:
        if t.index == n:
            return t.val
        t = t.next

    return None


def set(t, n, value):
    prev = None
    cur = t
    while cur and cur.val:
        if cur.index == n:
            cur.val = value
            return
        prev = cur
        cur = cur.next

    new = node(n, value)
    if prev:
        prev.next = new
    else:
        cur.val = value
        cur.index = n


def str(t):
    while t:
        print(t.val, end=" ")
        t = t.next

    print()

'''
zbior = node()
init(zbior)
set(zbior, 5, 1)
set(zbior, 2, 2)
set(zbior, 0, 4)
str(zbior)
'''
test = node()
str(test)
init(test)
str(test)
