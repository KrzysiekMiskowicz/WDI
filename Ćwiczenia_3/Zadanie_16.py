import random
N = 1000

def is_primary(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    divider = 5
    while divider*divider <= n:
        if n % divider == 0 or n % (divider+2) == 0:
            return False
        divider += 6

    return True

'''
def is_primary(n, array):
    for i in range(n+1):
        array.append(True)

    array[0] = False
    array[1] = False
    for i in range(2, int(n**0.5)+1):
        if array[i] == True:
            counter = 2
            while counter*i <= n:
                array[counter*i] = False
                counter += 1

primary = []
is_primary(1000, primary)
'''

t = []
for i in range(N):
    t.append(random.randrange(1000, 10000))

a1 = 1
a2 = 1
result = is_primary(t[1])
if result:
    while a1+a2 <= N:
        if a1+a2 == N:
            if is_primary(t[a2]):
                result = False
                break
        a1, a2 = a2, a1+a2

    if result:
        result = False
        for i in t:
            if is_primary(i):
                result = True
                break

print(result)




