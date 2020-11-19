import random
N = 100

def amplitude(t):
    min = max = t[0]

    for i in range(1, N):
        if t[i] > max:
            max = t[i]
        else:
            if t[i] < min:
                min = t[i]

    return max-min

random_numbers = []
for i in range(N):
    random_numbers.append(random.randrange(1, 151))
print(amplitude(random_numbers))




