def waga(odwazniki, n, do_odwarzenia):
    if do_odwarzenia == 0:
        return True

    if len(odwazniki) == n:
        return False

    return waga(odwazniki, n+1, do_odwarzenia-odwazniki[n]) or \
           waga(odwazniki, n+1, do_odwarzenia) or \
           waga(odwazniki, n+1, do_odwarzenia+odwazniki[n])


odwazniki = [10, 5, 2, 1]

for i in range(21):
    print(i, waga(odwazniki, 0, i))