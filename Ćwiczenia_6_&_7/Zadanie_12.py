'''
def rozklad(n, t, s = 0):
    if s == n:
        print(t, "+")
        return

    for i in range(1, n-s+1):
        #Nie dodawałem append tylko wywoływałem funkcję z arg (t+[i]), dlatego po wywołaniu funkcji nie należy t = t[:-1]
        rozklad(n, t+[i], s+i)
        #t = t[:-1]

    return
'''

'''
def rozklad(n, str):
    if n == 0:
        print(str, "+")
        return

    for i in range(1, n+1):
        #print(i, s, t)
        rozklad(n - i, str + " " + chr(48 + i))
        #print(i, s, t)
        #t = t[:-1]

    return
'''
def rozklad(n, t):
    if n == 0:
        print(t)
        return

    for i in range(1, n+1):
        #Nie dodawałem append tylko wywoływałem funkcję z arg (t+[i]), dlatego po wywołaniu funkcji nie należy t = t[:-1]
        rozklad(n-i, t+[i])
        #t = t[:-1]

    return
t = []
rozklad(6, t)

