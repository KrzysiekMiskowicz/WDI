class hetman:
    def __init__(self, w, k):
        self.w = w
        self.k = k

class dane:
    def __init__(self, N):
        self.N = N
        self.t = [hetman(-1, -1) for _ in range(100)]
        for i in range(self.N):
            w = int(input("Podaj wiersz -> "))
            k = int(input("Podaj kolumne -> "))
            self.t[i] = hetman(w, k)

def szach(t):
    for i in range(len(t)):
        if t[i].w < 0 or t[i].k < 0:
            break
        for j in range(i+1, len(t)):
            if t[j].w < 0 or t[j].k < 0:
                break
            if t[i].w == t[j].w or t[i].k == t[j].k or abs(t[i].w - t[j].w) == abs(t[i].k - t[j].k):
                return True

    return False


d = dane(3)
print(szach(d.t))

