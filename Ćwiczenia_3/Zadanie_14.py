import random
MAX = 100

def reverse_geometric_substring(string):
    current_length = 1
    max_length = 1
    for index in range(0, MAX - max_length):
        for repeat in range(index+1, MAX):
            if string[index] == string[repeat]:
                while index+current_length < MAX and repeat-current_length > 0 and string[index+current_length] == string[repeat-current_length]:
                    current_length += 1

                max_length = max(max_length, current_length)
                current_length = 1

    return max_length

random_numbers = []
for i in range(MAX):
    random_numbers.append(random.randrange(100, 999))
print(reverse_geometric_substring(random_numbers))