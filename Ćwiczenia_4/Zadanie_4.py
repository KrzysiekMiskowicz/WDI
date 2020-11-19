import random

MAX = 5
tab = [[random.randrange(1, 100) for i in range(MAX)] for j in range(MAX)]

for i in tab:
    print(i)

c_max = -1
c_index = -1
l_min = -1
l_index = -1

for i in range(MAX):
    l_s = 0
    c_s = 0
    for j in range(MAX):
        l_s += tab[i][j]
        c_s += tab[j][i]

    if l_min < 0:
        l_min = l_s
        l_index = i
    else:
        if l_min > l_s:
            l_min = l_s
            l_index = i

    if c_max < c_s:
        c_max = c_s
        c_index = i
print(c_max)
print(l_min)
print("[", l_index, ",", c_index, "] -> ", c_max/l_min)




