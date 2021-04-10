def odd_binary_ones(n):
    ones = 0
    while n > 0:
        if n % 2 == 1:
            ones += 1
        n //= 2

    return ones % 2 == 1

def remove_one_row_and_two_columns(t):
    n = len(t)
    for r in range(n):
        for r1 in range(n-1):
            for r2 in range(r1+1, n):
                result = True
                for i in range(n):
                    if i != r:
                        for j in range(n):
                            if j != r1 and j != r2:
                                if not odd_binary_ones(t[i][j]):
                                    result = False
                                    break
                    if not result:
                        break

                if result:
                    return True

    return False


t = [ [1, 1, 3, 3],
      [3, 3, 3, 3],
      [1, 1, 3, 3],
      [1, 3, 3, 3] ]

print(remove_one_row_and_two_columns(t))