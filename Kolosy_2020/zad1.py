#Krzysztof Miśkowicz

def multi(T):
    n = len(T)
    max_repeats = 0
    for LEN in range(1, int(n/2) + 1):
        for begin in range(n-LEN):

            current_repeats = 0
            for i in range(begin, n, LEN):
                if T[i:i+LEN] == T[i+LEN:i+2*LEN]:
                    current_repeats += 1
                    max_repeats = max(max_repeats, current_repeats+1)
                else:
                    current_repeats = 0

    return max_repeats

A = "ABAABAABA"
print(multi(A))
