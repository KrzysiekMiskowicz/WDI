max_iteracji = 0
max_indeks = 0
for i in range(2, 10000):
    An = i
    liczba_iteracji = 0
    while An != 1:
        liczba_iteracji += 1
        An = (An%2)*(3*An + 1)+(1 - An%2)*An/2
    if liczba_iteracji > max_iteracji:
        max_iteracji = liczba_iteracji
        max_indeks = i
    else:
        pass
print("Maksymalna liczba iteracji to", max_iteracji,  "dla A0 =", max_indeks)