def longest_repeatitions_in_row(t):
    n = len(t)
    row = None
    max_repeatitions = 0
    for i in range(n):
        max_repeatitions_in_current_row = 1
        current_repeatitions = 1
        for j in range(n-1):
            if t[i][j-1] == t[i][j]:
                current_repeatitions += 1
            else:
                current_repeatitions = 1
                max_repeatitions_in_current_row = max(max_repeatitions_in_current_row, current_repeatitions)

        max_repeatitions_in_current_row = max(max_repeatitions_in_current_row, current_repeatitions)
        if max_repeatitions_in_current_row > max_repeatitions:
            max_repeatitions = max_repeatitions_in_current_row
            row = i

    return row


t = [[3, 3, 2],
     [3, 3, 3],
     [3, 3, 2]]

print(longest_repeatitions_in_row(t))