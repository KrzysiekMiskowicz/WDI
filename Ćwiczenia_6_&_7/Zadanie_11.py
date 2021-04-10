def found_N_product_it(t, p):
    n = len(t)
    for i in range(1, int(2**n)+1):
        shift_b = 1
        s = 1
        N = []
        for j in reversed(range(n)):
            if (i & shift_b) != 0:
                s *= t[j]
                N.append(t[j])
            shift_b *= 2

        if p == s:
            for j in N:
                print(j, end=" ")
            print()



def found_N_product_re(t, p, N, n):
    sum = 1
    for i in N:
        sum *= i
    if sum == p:
        for i in N:
            print(i, end=" ")
        print()
        return
    elif sum > p:
        return

    if n == len(t)-1:
        return

    for i in range(n+1, len(t)):
        N.append(t[i])
        found_N_product_re(t, p, N, i)
        #if len(N) != 0:
        N.pop()

t = [9, 2, 4, 5, 6, 3, 5]
N = []
#found_N_product_it(t, 6)
found_N_product_re(t, 6, N, -1)


























