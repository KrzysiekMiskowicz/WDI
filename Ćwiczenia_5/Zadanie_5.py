MAX = 10

class punkt:
    def __init__(self, x = -1, y = -1):
        self.x = x
        self.y = y

class dane:
    def __init__(self, N):
        self.t = [punkt() for _ in range(MAX)]
        for i in range(N):
            x = int(input("Podaj wsp x -> "))
            y = int(input("Podaj wsp y -> "))
            self.t[i] = punkt(x, y)


def szukaj_kwadratu(t):
    pozycje = [[False for _ in range(MAX)] for _ in range(MAX)]
    for i in t:
        if i.x < 0 and i.y < 0:
            break
        pozycje[i.x][i.y] = True

    for ld in t:
        if ld.x < 0 or ld.y < 0:
            break
        pg = punkt(ld.x+1, ld.y+1)
        while pg.x < MAX and pg.y < MAX:
            if pozycje[pg.x][pg.y] and pozycje[ld.x][pg.y] and pozycje[pg.x][ld.y]:
                pkt_w_kwadracie = False
                for i in range(ld.y+1, pg.y):
                    for j in range(ld.x+1, pg.x):
                        if pozycje[i][j]:
                            pkt_w_kwadracie = True
                            break

                    if pkt_w_kwadracie:
                        break

                if not pkt_w_kwadracie:
                    return True

            pg.x += 1
            pg.y += 1

    return False


d = dane(5)
print(szukaj_kwadratu(d.t))

