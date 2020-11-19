import random

MAX = 5
tab = [[random.randrange(-10, 10) for i in range(MAX)] for j in range(MAX)]

for i in tab:
    print(i)

c_max_plus = 0
c_max_minus = 0
c_index_plus = -1
c_index_minus = -1

l_min_plus = 0
l_min_minus = 0
l_index_plus = -1
l_index_minus = -1

for i in range(MAX):
    l_s = 0
    c_s = 0
    for j in range(MAX):
        l_s += tab[i][j]
        c_s += tab[j][i]

    if l_min_plus == 0:
        if l_s > 0:
            l_min_plus = l_s
            l_index_plus = i
    else:
        if l_min_plus > l_s > 0:
            l_min_plus = l_s
            l_index_plus = i

    if l_min_minus == 0:
        if l_s < 0:
            l_min_minus = l_s
            l_index_minus = i
    else:
        if l_min_minus < l_s < 0:
            l_min_minus = l_s
            l_index_minus = i

    if c_max_plus < c_s:
        c_max_plus = c_s
        c_index_plus = i

    if c_max_minus > c_s:
        c_max_minus = c_s
        c_index_minus = i


print("Dzielna + -> ", c_max_plus)
print("Dzielna - -> ", c_max_minus)
print("Dzielnik + -> ", l_min_plus)
print("Dzielnik - -> ", l_min_minus)
if l_min_plus != 0 and l_min_minus != 0:
    if c_max_plus / l_min_plus >= c_max_minus / l_min_minus:
        print("[", l_index_plus, ",", c_index_plus, "] -> ", c_max_plus / l_min_plus)
    else:
        print("[", l_index_minus, ",", c_index_minus, "] -> ", c_max_minus / l_min_minus)
elif l_min_plus != 0:
    print("[", l_index_plus, ",", c_index_plus, "] -> ", c_max_plus / l_min_plus)
elif l_min_minus != 0:
    print("[", l_index_minus, ",", c_index_minus, "] -> ", c_max_minus / l_min_minus)
else:
    pass

