for i in range(1, 1000000):
    number = i
    dividers_number = 1

    temp_number = number
    digits_sum = 0
    while temp_number > 0:
            digits_sum += temp_number % 10
            temp_number //= 10

    dividers_sum = 0
    while number % 2 == 0:
        dividers_sum += 2
        if dividers_sum > digits_sum:
            break
        dividers_number += 1
        number //= 2

    divider = 3
    while number != 1 and digits_sum > dividers_sum:
        if number % divider == 0:
            dividers_number += 1
            number //= divider

            temp_number = divider
            while temp_number > 0:
                dividers_sum += temp_number % 10
                temp_number //= 10

            if dividers_sum > digits_sum:
                break

        else:
            divider += 2

    if dividers_sum == digits_sum and dividers_number > 2:
        print(i)
