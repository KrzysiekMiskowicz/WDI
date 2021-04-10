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
                    if self.next:
                        self.val = self.next.val
                        self.next = self.next.next
                    else:
                        self = None
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


zbior = node()
zbior.__str__()
zbior.__add__(5)
zbior.__add__(9)
zbior.__add__(7)
zbior.__add__(11)
zbior.__str__()
zbior.__delete__(11)
zbior.__str__()

zbior = node(5)
zbior.__str__()
zbior.__delete__(5)
zbior.__str__()