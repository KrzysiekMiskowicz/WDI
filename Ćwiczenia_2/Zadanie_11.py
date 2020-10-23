number = int(input("Press a number -> "))

result = False
An = 2
while An*An <= number:
    if number % An == 0 and number != An:
        result = True
        break
    An = 3*An + 1

print(result)