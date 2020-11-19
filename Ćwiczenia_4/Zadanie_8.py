MAX = 4

#zakładam że elementy tablicy różne od 0
def longest_substring(tab):
    i = MAX-3
    max_sub = 2
    for i in range(MAX-2):
        q = tab[1][i+1] / tab[0][i]
        current_sub = 2
        j = i+2
        while j < MAX:
            if tab[j-i][j] / tab[j-i-1][j-1] != q:
                break
            current_sub += 1
            j += 1

        max_sub = max(current_sub, max_sub)

        q = tab[i+1][1] / tab[i][0]
        current_sub = 2
        j = i+2
        while j < MAX:
            if tab[j][j-i] / tab[j-1][j-i-1] != q:
                break
            current_sub += 1
            j += 1

        max_sub = max(current_sub, max_sub)

    return max_sub

t = [[2, 2, 3, 4],
     [1, 1, 4, 4],
     [1, 2, 1, 8],
     [2, 2, 3, 2]]
print(longest_substring(t))


