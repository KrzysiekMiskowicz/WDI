#kłopot skicingu tablicy dwuwymiarowej
'''
def wyznacznik(M):
    n = len(M)
    if n == 2:
        return M[0][0]*M[1][1] - M[1][0]*M[0][1]

    max_zeros_row = -1
    max_zeros = -1
    for r in range(n):
        zeros = 0
        for c in range(n):
            if M[r][c] == 0:
                zeros += 1

        if zeros > max_zeros:
            max_zeros = zeros
            max_zeros_row = r

    sum = 0
    for c in range(n):
        temp = []
        for i in range(n):
            if i != max_zeros_row:
                row = []
                for j in range(n):
                    if j != c:
                        row.append(M[i][j])

                temp.append(row)
        sum += M[max_zeros_row][c] * (-1)**(max_zeros_row+c) * wyznacznik(temp)

    return sum

'''

def wyznacznik(M):
    n = len(M)
    if n == 2:
        return M[0][0]*M[1][1] - M[1][0]*M[0][1]

    suma = 0
    for r in range(n):
        #T = [ 0 for _ in range(n-1) [for _ in range(n-1)] ]
        for c in range(1, n):
            row = []
            for i in range(n):
                if i == r:
                    continue
                else:
                    row += [M[i][c]]
            T += [row]
            print(T)
        suma += M[r][0] * (-1)**r * wyznacznik(T)

    return suma

t = [[2, 0, 0], [0, 2, 0], [0, 7, 2]]
print(wyznacznik(t))
#p = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#print(p[1:4])