import random
MAX = 100

def longest_substring(string):
    current_length = 1
    max_length = 1
    for index in range(1, MAX):
        if string[index] <= string[index-1]:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
        else:
            current_length += 1

    return max(current_length, max_length)

random_numbers = []
for i in range(MAX):
    random_numbers.append(random.randrange(1, 150))
print(longest_substring(random_numbers))