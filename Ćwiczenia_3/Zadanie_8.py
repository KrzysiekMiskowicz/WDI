MAX = 1000
odd = []

for i in range(1000):
    result = True
    while i > 0:
        if i % 2 == 0:
            result = False
            break
        i //= 10

    odd.append(result)

odd[0] = False
for i in range(MAX):
    if odd[i]:
        print(i, True)