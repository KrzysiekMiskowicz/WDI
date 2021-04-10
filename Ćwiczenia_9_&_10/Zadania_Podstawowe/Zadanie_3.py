class node:
    def __init__(self, x = 0):
        self.val = x
        self.next = None


    def __contains__(self, item):
        while self is not None:
            if self.val == item:
                return True
            self = self.next

        return False


    def __add__(self, other):
        if self.__contains__(other):
            return False

        p = None
        while self is not None:
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


    def __delete__(self, instance):
        p = None
        while self is not None:
            if self.val == instance:
                if p is None:
                    self.val = self.next.val
                    self.next = self.next.next
                    return True
                else:
                    p.next = self.next
                    return True
            p = self
            self = self.next

        return False


    def __str__(self):
        while self:
            print(self.val, end=", ")
            self = self.next

        print()

def merge(n1, n2):
    if n1 is None and n2 is None:
        return
    elif n1 is None:
        return n2
    elif n2 is None:
        return n1

    if n1.val > n2.val:
        merged = node(n2.val)
        n2 = n2.next
    else:
        merged = node(n1.val)
        n1 = n1.next

    tail = merged

    while n1 is not None and n2 is not None:
        if n1.val > n2.val:
            merged.next = n2
            n2 = n2.next
        else:
            merged.next = n1
            n1 = n1.next
        merged = merged.next

    if n1 is not None:
        merged.next = n1
    else:
        merged.next = n2

    return tail


def mergeR(n1, n2):
    if n1 is None:
        return n2
    if n2 is None:
        return n1

    if n1.val > n2.val:
        n2.next = mergeR(n1, n2.next)
        return n2
    else:
        n1.next = mergeR(n1.next, n2)
        return n1

a = node(1)
a.__add__(3)
a.__add__(5)
a.__add__(7)
b = node(0)
b.__add__(2)
b.__add__(5)
b.__add__(7)
b.__add__(8)

c = merge(a, b)
c.__str__()
