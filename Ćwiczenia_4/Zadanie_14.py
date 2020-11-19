MAX_1 = 3
MAX_2 = 5

def is_matching(n1, n2):
    n1_bin_1 = n2_bin_1 = 0
    while n1 > 0 or n2 > 0:
        if n1 % 2 == 1:
            n1_bin_1 += 1
        if n2 % 2 == 1:
            n2_bin_1 += 1
        n1 //= 2
        n2 //= 2

    return n1_bin_1 == n2_bin_1


def find_matching_numbers(t1, t2):
    max = 0
    pos_x = -1
    pos_y = -1
    for i in range(len(t2) - len(t1)):
        for j in range(len(t2) - len(t1)):
            current = 0
            for a in range(len(t1)):
                for b in range(len(t1)):
                    if is_matching(t1[a][b], t2[i+a][j+b]):
                        current += 1

            if current > max:
                max = current
                pos_x = i
                pos_y = j

    print("[", pos_x, ",", pos_y, "]")
    return max

t1 = [[1, 8, 4],
     [3, 9, 17],
     [1, 8, 4]]

t2 = [[1, 8, 4, 7, 21],
      [4, 4, 1, 2, 7],
      [1, 1, 5, 4, 5],
      [5, 1, 9, 2, 7],
      [3, 3, 3, 3, 3]]

print(find_matching_numbers(t1, t2))
