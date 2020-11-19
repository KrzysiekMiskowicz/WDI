MAX = 6

def find_square(tab, k):
    for i in range(MAX-2):
        for j in range(MAX-2):
            a = 2
            while i+a < MAX and j+a < MAX:
                print("[", int((i+i+a)/2), ",", int((j+j+a)/2), "] ->", tab[i][j]*tab[i+a][j]*tab[i][j+a]*tab[i+a][j+a])
                if tab[i][j]*tab[i+a][j]*tab[i][j+a]*tab[i+a][j+a] == k:
                    print("[", int((i+i+a)/2), ",", int((j+j+a)/2), "]")
                    return
                a += 2


t = [[2, 2, 2, 2, 5, 6],
     [1, 1, 4, 4, 6, 5],
     [1, 2, 1, 7, 7, 3],
     [2, 2, 3, 2, 4, 2],
     [4, 2, 1, 4, 4, 1],
     [1, 2, 4, 4, 13, 1]]
find_square(t, 78)


