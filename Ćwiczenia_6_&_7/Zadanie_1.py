def waga(odwazniki, n, do_odwarzenia):
    if do_odwarzenia == 0:
        return True
    elif do_odwarzenia < 0:
        return False

    if len(odwazniki) == n:
        return False

    return waga(odwazniki, n+1, do_odwarzenia - odwazniki[n]) or waga(odwazniki, n+1, do_odwarzenia)


odwazniki = [5, 4, 3, 2, 1, 10]

for i in range(30):
    print(i, waga(odwazniki, 0, i))
