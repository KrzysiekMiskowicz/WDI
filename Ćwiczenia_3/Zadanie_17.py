import random
N = 100

def f(t):
    only_max = True
    only_min = True
    min = max = t[0]

    for i in range(1, N):
        if t[i] == max:
            only_max = False
        elif t[i] > max:
            only_max = True
            max = t[i]

        if t[i] == min:
            only_min = False
        elif t[i] < max:
            only_min = True
            min = t[i]

    return only_max and only_min

random_numbers = []
for i in range(N):
    random_numbers.append(random.randrange(1, 151))
print(f(random_numbers))




