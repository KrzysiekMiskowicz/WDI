def waga(odwazniki, n, do_odwarzenia, uzycia):

    if len(odwazniki) == n:
        if do_odwarzenia == 0:
            print(uzycia)
    else:
        waga(odwazniki, n+1, do_odwarzenia-odwazniki[n], uzycia+'L')
        waga(odwazniki, n+1, do_odwarzenia, uzycia+'0')
        waga(odwazniki, n+1, do_odwarzenia+odwazniki[n], uzycia+'P')


odwazniki = [10, 5, 2, 1]

waga(odwazniki, 0, 12, "")