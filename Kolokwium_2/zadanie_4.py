#Krzysztof Miśkowicz

def chess(T):
    n = len(T)
    fields = [count_line(T, i // n) + count_column(T, i % n) for i in range(n * n)]
    row1, row2, col1, col2 = None, None, None, None
    max_sum = None
    for i in range(n*n-1):
        for j in range(i+1, n*n):

            current_sum = fields[i] + fields[j]

            if i//n == j//n:
                current_sum -= count_line(T, i // n)
            elif i%n == j%n:
                current_sum -= count_column(T, i % n)
            else:
                current_sum -= T[i // n][i % n] + T[j // n][j % n] + T[i // n][j % n] + T[i // n][j % n]

            current_sum -= T[i // n][i % n] + T[j // n][j % n]

            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
                row1, row2, col1, col2 = i//n, j//n, i%n, j%n

    #print(max_sum) #nie rozumiem jak zwracac sume
    return (row1, col1, row2, col2, max_sum)


def count_line(t, l):
    sum = 0
    for i in range(len(t)):
        sum += t[l][i]

    return sum


def count_column(t, c):
    sum = 0
    for i in range(len(t)):
        sum += t[i][c]

    return sum


print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0)
#print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]])) # (2,3,3,1) suma=35
