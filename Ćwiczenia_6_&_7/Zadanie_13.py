def Hanoi(n, A, B, C):
    if n == 1:
        C.append(A.pop()) #przenosimy z A na C
        #print(A, B, C, "+")
        return 1
    else:
        s = 0
        s += Hanoi(n-1, A, C, B) # przenosimy z A na B
        C.append(A.pop())
        s += 1 + Hanoi(n-1, B, A, C) # przenosimy z B na C
        return s

A = [4, 3, 2, 1]
B = []
C = []
print(Hanoi(4, A, B, C))