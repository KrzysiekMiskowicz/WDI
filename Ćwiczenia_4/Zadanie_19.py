import random
MAX = 5

#dla naturalnych
def find_product_on_knight_moves(t, product):
    matches = 0
    moves = [[2, -1], [2, 1], [1, -2], [1, 2]]
    for i in range(len(t)):
        for j in range(len(t)):
            for a in moves:
                if i+a[0] < len(t) and 0 <= j+a[1] < len(t) and t[i][j]*t[i+a[0]][j+a[1]] == product:
                    matches += 1
                    print(matches, "[", j, ",", i, "]\t", "[", j+a[1], ",", i+a[0], "]")


t = [[random.randrange(1, 10) for _ in range(MAX)] for _ in range(MAX)]
for i in t:
    print(i)
print(find_product_on_knight_moves(t, 4))