class node:
    def __init__(self, x = None):
        self.val = x
        self.next = None

    def __contains__(self, item):
        while self and self.val:
            if self.val == item:
                return True
            self = self.next

        return False

    def __add__(self, other):
        if self.__contains__(other):
            return False

        p = None
        while self and self.val:
            p = self
            self = self.next

        if p is None:
            self.val = other
            self.next = None
        else:
            p.next = node()
            p.next.val = other
            p.next.next = None
        return True

    def __str__(self):
        while self:
            print(self.val, end=" ")
            self = self.next

        print()


def split(l, t):
    while l:
        t[l.val % 10].__add__(l.val)
        l = l.next


def merge(t):
    first = True
    merged = node()
    merged.__str__()
    head = merged
    for i in t:
        while i and i.val:
            if first:
                first = False
                merged.val = i.val
            else:
                merged.next = i
                merged = merged.next
            i = i.next

    return head


tab = [node() for _ in range(10)]
list = node(4)
list.__add__(6)
list.__add__(3)
list.__add__(16)
list.__add__(0)
list.__str__()

split(list, tab)
test = merge(tab)
test.__str__()