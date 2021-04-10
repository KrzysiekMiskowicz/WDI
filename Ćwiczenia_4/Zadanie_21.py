def delete_2_rooks(t, w):
    n = len(t)
    max_free_fields = 0
    c1, c2 = None, None
    for i in range(n-1):
        for j in range(i+1, n):
            current_free_fields = 0
            for empty_rows in range(n):
                is_empty = True
                for reserved_rows in range(n):
                    if reserved_rows == i or reserved_rows == j:
                        continue
                    if empty_rows == w[reserved_rows]:
                        is_empty = False
                        break

                if is_empty:
                    current_free_fields += t[empty_rows][i] + t[empty_rows][j]

            if current_free_fields > max_free_fields:
                max_free_fields = current_free_fields
                c1, c2 = i, j

    print("{}, {}".format(c1, c2))
    return max_free_fields


t =[[4, 3, 0, 4, 0],
    [8, 2, 2, 1, 4],
    [4, 5, 3, 7, 3],
    [4, 4, 4, 4, 4],
    [2, 4, 5, 4, 0]]

w = [1, 1, 3, 2, 4]

print(delete_2_rooks(t, w))
