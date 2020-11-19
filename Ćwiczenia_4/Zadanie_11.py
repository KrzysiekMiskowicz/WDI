MAX = 4

def is_friend(n1, n2):
    n1_digits = [False for _ in range(10)]
    n2_digits = [False for _ in range(10)]
    tmp = n1
    while tmp > 0:
        n1_digits[tmp % 10] = True
        tmp //= 10

    tmp = n2
    while tmp > 0:
        n2_digits[tmp % 10] = True
        tmp //= 10

    return n1_digits == n2_digits


def find_touched_friends(t):
    result = 0
    for i in range(MAX):
        for j in range(MAX):
            only_friends = True
            set_ref = False
            ref = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if 0 <= i+a < MAX and 0 <= j+b < MAX and (a != 0 or b != 0):
                        if not set_ref:
                            set_ref = True
                            ref = t[i+a][j+b]
                        else:
                            if not is_friend(ref, t[i+a][j+b]):
                                only_friends = False
                                break

                if not only_friends:
                    break

            if only_friends:
                result += 1

    return result


t = [ [3, 3, 3, 4],
      [3, 1, 3, 3],
      [3, 3, 3, 1],
      [3, 3, 1, 1]]


print(find_touched_friends(t))