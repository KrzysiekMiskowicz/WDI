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

    def __reversed__(self):
        if not self:
            return

        head = self
        reverse = node()
        reverse.val = self.val
        reverse.next = None
        self = self.next
        while self:
            a = reverse
            reverse = node(self.val)
            reverse.next = a
            self = self.next

        head.val = reverse.val
        head.next = reverse.next


a = node(1)
a.__add__(3)
a.__add__(5)
a.__add__(7)
a.__str__()
a.__reversed__()
a.__str__()