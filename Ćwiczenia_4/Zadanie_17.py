def find_max_surroundings(t):
    l = None
    c = None
    max_sum = 0
    for i in range(len(t)):
        for j in range(len(t)):
            current_sum = 0
            for a in range(-1, 2):
                if 0 <= i+a < len(t):
                    for b in range(-1, 2):
                        if 0 <= j+b < len(t) and (a != 0 or b != 0):
                            current_sum += t[i+a][b+j]
                if current_sum > max_sum:
                    max_sum = current_sum
                    l = i
                    c = j

    print('({}, {})' .format(c, l))
    return max_sum

t = [ [2, 3, 4, 5, 4],
      [1, 2, 3, 6, 3],
      [4, 5, 1, 4, 2],
      [4, 2, 6, 7, 1],
      [2, 1, 2, 9, 2]  ]
print(find_max_surroundings(t))