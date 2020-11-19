MAX = 1000
odd = []

for i in range(1000):
    result = False
    while i > 0:
        if i % 2 == 1:
            result = True
            break
        i //= 10
        
    odd.append(result)

for i in range(MAX):
    if odd[i]:
        print(i, True)