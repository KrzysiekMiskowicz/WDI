#Krzysztof Miśkowicz

def distance(T):
    n = len(T)
    most_zeros_start = 0
    most_zeros_start_r = -1
    most_ones_start = 0
    most_ones_start_r = -1
    min_repeat_start = 0
    min_repeat_start_r = 0
    for i in range(n):
        if T[i][0] == 1:
            current = 1
        else:
            current = 0
        repeats = 0

        for j in range(n):
            if T[i][j] != current:
                break
            repeats += 1

        if i == 0:
            min_repeat_start = repeats
            min_repeat_start_r = 0

        if repeats < min_repeat_start:
            min_repeat_start = repeats
            min_repeat_start_r = i

        if current == 1 and repeats > most_ones_start:
            most_ones_start = repeats
            most_ones_start_r = i

        elif current == 0 and repeats > most_zeros_start:
            most_zeros_start = repeats
            most_zeros_start_r = i

    if most_ones_start_r == -1:
        result = abs(most_zeros_start_r - min_repeat_start_r)
    elif most_zeros_start_r == -1:
        result = abs(most_ones_start_r - min_repeat_start_r)
    else:
        result = abs(most_ones_start_r - most_zeros_start_r)

    return result

T = [ [1, 1, 1, 1],
      [1, 1, 1, 0],
      [1, 1, 1, 0],
      [1, 1, 0, 0] ]

print(distance(T))