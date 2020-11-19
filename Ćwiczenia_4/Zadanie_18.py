import random
MAX = 5

#dla naturalnych
def max_column_or_line_substring(t):
    max_length = 3
    max_substring = 0
    pos_x = -1
    pos_y = -1
    lines_substring = 0
    columns_substring = [0 for _ in range(len(t))]
    for i in range(len(t)):
        for j in range(len(t)):
            if j == 0:
                counter = 0
                while j+counter < len(t) and counter < max_length:
                    lines_substring += t[i][j+counter]
                    counter += 1
            else:
                if j+max_length-1 < len(t):
                    lines_substring -= t[i][j-1]
                    lines_substring += t[i][j+max_length-1]
                else:
                    lines_substring -= t[i][j]

            if i == 0:
                counter = 0
                while i+counter < len(t) and counter < max_length:
                    columns_substring[j] += t[i+counter][j]
                    counter += 1
            else:
                if i+max_length-1 < len(t):
                    columns_substring[j] -= t[i-1][j]
                    columns_substring[j] += t[i+max_length-1][j]
                else:
                    columns_substring[j] -= t[i-1][j]

            if max_substring < columns_substring[j] or max_substring < lines_substring:
                max_substring = max(max_substring, columns_substring[j], lines_substring)
                pos_x = j
                pos_y = i

    print("[", pos_x, ",", pos_y, "]")
    return max_substring

t = [[random.randrange(1, 10) for _ in range(MAX)] for _ in range(MAX)]
for i in t:
    print(i)
print(max_column_or_line_substring(t))