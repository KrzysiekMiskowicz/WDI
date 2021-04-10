def multiple_of_square_of_natural_number(n):
    divider = 2
    multiple = 2
    while divider * divider * 2 <= n:
        while divider * divider * multiple <= n:
            if divider * divider * multiple == n:
                return True
            multiple += 1

        multiple = 2
        divider += 1

    return False


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
                                if not multiple_of_square_of_natural_number(t[i][j]):
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