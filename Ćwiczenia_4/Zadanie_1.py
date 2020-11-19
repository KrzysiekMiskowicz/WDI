MAX = 10
tab = [[0 for i in range(MAX)] for j in range(MAX)]


n = 1
l = 0
c = -1
dir = 0
a = MAX
while a > 0:
    a_shift = a
    while a_shift > 0:
        if dir == 0:
            c += 1
        elif dir == 1:
            l += 1
        elif dir == 2:
            c -= 1
        elif dir == 3:
            l -= 1
        else:
            pass
        tab[l][c] = n
        n += 1
        a_shift -= 1

    if dir % 2 == 0:
        a -= 1
    dir = (dir + 1) % 4


for i in tab:
    print(i)
