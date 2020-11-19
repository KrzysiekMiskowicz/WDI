max_numbers = []
for i in range(10):
    max_numbers.append(0)

counter = 0
while True:
    number = int(input("Wprowadz numer -> "))
    if number == 0 and counter >= 10:
        break
    if number > max_numbers[9]:
        i = 8
        while number > max_numbers[i] and i >= 0:
            i -= 1

        i += 1
        for j in reversed(range(i+1, 10)):
            max_numbers[j] = max_numbers[j-1]

        max_numbers[i] = number
    counter += 1

for i in max_numbers:
    print(i, end=" ")
