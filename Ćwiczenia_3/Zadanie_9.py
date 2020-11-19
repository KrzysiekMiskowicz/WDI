import random
MAX = 100

def jumps(numbers):
    available = []
    available.append(True)
    for i in range(1, MAX):
        available.append(False)

    for i in range(MAX):
        if available[i]:
            tmp_number = numbers[i]
            divider = 2
            while tmp_number > 1:
                if tmp_number % divider == 0:
                    if i+divider == MAX-1:
                        return True
                    if i+divider < MAX:
                        available[i + divider] = True
                    while tmp_number % divider == 0:
                        tmp_number //= divider
                divider += 1

    return False

random_numbers = []
for i in range(MAX):
    random_numbers.append(random.randrange(2, 200))

print(jumps(random_numbers))