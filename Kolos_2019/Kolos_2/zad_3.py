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


def remove_longest_substring(p):
    if p is None or p.val is None:
        return 0

    head = p
    max_sub_len = 0
    max_sub_index = -1
    max_sub = False
    current_index = 0
    current_sub = 0
    prev = None

    while p is not None and p.val is not None:
        if prev is None:
            current_sub = 1
            max_sub = True
            max_sub_index = 0
        else:
            if p.val == prev.val:
                current_sub += 1
            else:
                if current_sub > max_sub_len:
                    max_sub_len = current_sub
                    max_sub = True
                    max_sub_index = current_index - max_sub_len
                elif current_sub == max_sub_len:
                    max_sub = False
                current_sub = 1

        current_index += 1
        prev = p
        p = p.next

    if max_sub:
        p = head
        if max_sub_index == 0:
            for _ in range(max_sub_len):
                p = p.next

            head.val = p.val
            head.next = p.next
        else:
            for _ in range(max_sub_index-1):
                p = p.next

            head = p
            for _ in range(max_sub_len):
                p = p.next

            head.next = p.next
        return max_sub_len
    else:
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
list(a)

#[ 1 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ]


print(remove_longest_substring(a))
list(a)

#[ 1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ]

b = node(1)
add(b, 3)
add(b, 3)
add(b, 3)
add(b, 3)
add(b, 5)
add(b, 7)
add(b, 11)
add(b, 13)
add(b, 13)
add(b, 1)
add(b, 2)
add(b, 2)
add(b, 2)
add(b, 2)
add(b, 3)
add(b, 1)

list(b)
print(remove_longest_substring(b))
list(b)

while contain(b, 1):
    p = b
    remove(p, 1)

list(b)


