number1 = int(input("Press a number1 -> "))
number2 = int(input("Press a number2 -> "))
result = -1
for i in range(2, 16+1):
    base = i
    base_number1 = 0
    base_number2 = 0
    repeated_digits = False
    for test in range(2):
        digits_counter = 0
        new_digit = 0
        if test == 0:
            temp_number = number1
        else:
            temp_number = number2
        while temp_number > 0:
            new_digit = temp_number % base
            digit_value = 0
            while base_number1 >= base**digit_value or base_number2 >= base**digit_value:
                if new_digit == (base_number1 // base ** digit_value) % base and base_number1 >= base**digit_value:
                    repeated_digits = True
                    break
                if new_digit == (base_number2 // base ** digit_value) % base and base_number2 >= base**digit_value:
                    repeated_digits = True
                    break
                digit_value += 1

            if repeated_digits:
                break
            if test == 0:
                base_number1 += new_digit * base ** digits_counter
            else:
                base_number2 += new_digit * base ** digits_counter
            temp_number //= base
            digits_counter += 1

        if repeated_digits:
            break

    if repeated_digits == False:
        result = i
        break

print(result)
'''
    if repeted_digits:
        pass
    else:
        while base_number > 0:
            lsd = base_number % base  # least significant digit
            digit_value = 1
            while base_number >= base**digit_value:
                if lsd == (base_number // (base**digit_value)) % base:
                    repeted_digits = True
                    break
                digit_value += 1

            if repeted_digits:
                break
            base_number //= base
    if repeted_digits == False:
        print(base)
        break
'''

