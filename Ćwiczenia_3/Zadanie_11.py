import random
MAX = 100

def longest_arithmetic_substring(string):
    current_length = 2
    max_length = 2
    for index in range(2, MAX):
        if string[index] - string[index-1] == string[index-1] - string[index-2]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 2

    return max(max_length, current_length)

random_numbers = []
for i in range(MAX):
    random_numbers.append(random.randrange(1, 150))

print(longest_arithmetic_substring(random_numbers))