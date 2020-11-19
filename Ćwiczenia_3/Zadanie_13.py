import random
MAX = 100

def diffrence_arithmetic_substring(string):
    current_length = 2
    max_plus_length = 1
    max_minus_length = 1
    for index in range(2, MAX):
        if string[index] - string[index-1] == string[index-1] - string[index-2]:
            current_length += 1
        else:
            if string[index-1] - string[index-2] > 0 and current_length > max_plus_length:
                max_plus_length = current_length
            elif string[index-1] - string[index-2] < 0 and current_length > max_minus_length:
                max_minus_length = current_length
            current_length = 2

    if string[MAX-1] - string[MAX-2] > 0 and current_length > max_plus_length:
        max_plus_length = current_length
    elif string[MAX-1] - string[MAX-2] < 0 and current_length > max_minus_length:
        max_minus_length = current_length

    return max_plus_length - max_minus_length

random_numbers = []
for i in range(MAX):
    random_numbers.append(random.randrange(1, 151, 2))

print(diffrence_arithmetic_substring(random_numbers))